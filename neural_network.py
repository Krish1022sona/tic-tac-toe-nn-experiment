import game
import math_mine
import random
import data

random.seed(42)

class Neuron:
    def __init__(self):
        # Xavier initialization
        fan_in = 9  # number of inputs
        limit = math_mine.math.sqrt(6.0 / fan_in)

        self.weights = [random.uniform(-limit, limit) for _ in range(9)]
        self.bias = random.uniform(-0.1, 0.1) # it add to the value coming from behind it
        self.value = 0 # the value it is storing

    def forward(self, index): # pass the value * weight[index] from here
        return self.value * self.weights[index]

class NN:
    def __init__(self, number_of_inputs, number_of_outputs, number_of_hidden_layers, number_of_neurons_in_each_hidden_layer = 9):
        self.input_layer = [Neuron() for i in range(number_of_inputs)]
        self.output_layer = [Neuron() for i in range(number_of_outputs)]

        self.hidden_layers = [[Neuron() for j in range(number_of_neurons_in_each_hidden_layer)] for i in range(number_of_hidden_layers)]

        self.cross_entropies = []
        self.output_probab = []

    def predict(self, inputs):
        for i in range(9): # setting up the input layer
            self.input_layer[i].value = inputs[i]
        
        for i in range(9): # forward passing from input to hidden layer
            self.hidden_layers[0][i].value = math_mine.ReLU(sum([neuron.forward(i) for neuron in self.input_layer]) + self.hidden_layers[0][i].bias)

        for i in range(1, len(self.hidden_layers)): # forward passing in between the hidden layers
            for j in range(9): 
                self.hidden_layers[i][j].value = math_mine.ReLU(sum([neuron.forward(j) for neuron in self.hidden_layers[i-1]]) + self.hidden_layers[i][j].bias)
        
        for i in range(9): # forward pass from last hidden layer to output layer
            self.output_layer[i].value = sum([neuron.forward(i) for neuron in self.hidden_layers[len(self.hidden_layers) - 1]]) + self.output_layer[i].bias

        # finding softmax of the outputs
        self.output_probab = math_mine.softmax([neuron.value for neuron in self.output_layer])

        for i in range(9): # setting the softmax outputs in the output layer
            self.output_layer[i].value = self.output_probab[i]

    def best_move(self, board):
        valids = game.get_valid_moves(board)

        valid_probab = [self.output_probab[i] for i in range(9) if (i+1) in valids]

        return self.output_probab.index(max(valid_probab)) + 1

    def loss(self):
        return math_mine.cross_entropy_loss(self.cross_entropies)

    def train(self, test_data, output_data, learning_rate):
        # for experiment
        size = len(test_data)

        predicted_output_data = []
        self.cross_entropies = []

        hidden_layer_values_per_sample = [] # for storing hidden layer outputs
        hidden_layer_inputs_per_sample = [] # for storing hidden layer inputs


        # setting the data
        for i in range(len(test_data)):
            self.predict(test_data[i])
            predicted_output_data.append(self.output_probab[:])

            # FIX: Add epsilon to prevent log(0) error
            epsilon = 1e-15
            prob_value = max(self.output_layer[output_data[i] - 1].value, epsilon)
            self.cross_entropies.append(math_mine.cross_entropy(prob_value))

            hidden_layer_values_per_sample.append([neuron.value for neuron in self.hidden_layers[0]])
            hidden_layer_inputs_per_sample.append([sum([neuron.forward(i) for neuron in self.input_layer]) + self.hidden_layers[0][i].bias for i in range(9)])

        # print(self.loss())
        
        # for biases in the outputs
        for i, neuron in enumerate(self.output_layer): # ith output neuron's bias
            gradient_of_loss = 0

            for j in range(len(test_data)): # jth test case
                if output_data[j] == i+1: gradient_of_loss += predicted_output_data[j][i] - 1
                else: gradient_of_loss += predicted_output_data[j][i]
            
            neuron.bias = neuron.bias - gradient_of_loss * learning_rate / size

        #debug
        # print("Before weight update:")
        # print("Hidden layer weights for neuron 0:", self.hidden_layers[0][0].weights[:3])
        #debug
        
        # for the hidden layer, assuming only 1 hidden layer
        # formula same as above just multiply by output of corresponding node of hidden layer
        for i, neuron in enumerate(self.hidden_layers[0]):
            for w in range(9):
                gradient_of_loss = 0

                for j in range(len(test_data)):
                    neuron_val = hidden_layer_values_per_sample[j][i]
                    if output_data[j] == w+1: gradient_of_loss += (predicted_output_data[j][w] - 1) * neuron_val
                    else: gradient_of_loss += predicted_output_data[j][w] * neuron_val
                
                neuron.weights[w] -= gradient_of_loss * learning_rate / size

        #debug
        # print("After weight update:")  
        # print("Hidden layer weights for neuron 0:", self.hidden_layers[0][0].weights[:3])
        # print("Gradient was:", gradient_of_loss)
        #debug

        # for biases of hidden layer (assuming only 1 hidden layer)
        # this bias effects the Raw output of all the output nodes
        for i, neuron in enumerate(self.hidden_layers[0]):
            gradient_of_loss = 0
            for w in range(9):
                for j in range(len(test_data)):
                    neuron_input_val = hidden_layer_inputs_per_sample[j][i]
                    if output_data[j] == w+1: gradient_of_loss += (predicted_output_data[j][w] - 1) * math_mine.derivative_ReLU(neuron_input_val) * neuron.weights[w]
                    else: gradient_of_loss += predicted_output_data[j][w] * math_mine.derivative_ReLU(neuron_input_val) * neuron.weights[w]
                
            neuron.bias -= gradient_of_loss * learning_rate / size
        
        # for weights of the input layer
        # formula is same as before just multiply by the input value of the neuron whose weight we are tweaking
        for ind, input_neuron in enumerate(self.input_layer):
            for i, neuron in enumerate(self.hidden_layers[0]):
                gradient_of_loss = 0
                for w in range(9):
                    for j in range(len(test_data)):
                        neuron_input_val = hidden_layer_inputs_per_sample[j][i]
                        if output_data[j] == w+1: gradient_of_loss += (predicted_output_data[j][w] - 1) * math_mine.derivative_ReLU(neuron_input_val) * neuron.weights[w] * test_data[j][ind]
                        else: gradient_of_loss += predicted_output_data[j][w] * math_mine.derivative_ReLU(neuron_input_val) * neuron.weights[w] * test_data[j][ind]
                input_neuron.weights[i] -= gradient_of_loss * learning_rate / size

         
def start_game_AI(nn: NN):
    while True:
        print("Welcome to Tic Tac Toe AI")
        print("1-> New Game")
        print("2-> Quit")
        ch = int(input("Enter your Choice: "))

        if(ch == 2):
            print("Thanks For Playing")
            break
        if(ch == 1):
            print("Choose your Turn")
            print("1-> X [Goes First]")
            print("2-> O [Goes Second]")
            ch2 = int(input("Enter your Choice: "))

            if(ch2 == 1):
                board = game.generate_new_board()
                game.print_board(board)
                while True:
                    print("\n Player 1")
                    while game.play_turn(board, 1, int(input("Enter Your Position: "))) == -1: pass
                    print()
                    game.print_board(board)
                    
                    

                    result = game.is_game_finish(board)
                    if(result == 2):
                        print("\nDRAW\n")
                        break
                    if(result != 0): 
                        print("\nYou WON\n")
                        break
                    
                    state = [-1*x for x in game.get_board_state(board)]
                    # print(state)
                    nn.predict(state)
                    game.play_turn(board, -1, nn.best_move(board))
                    print()
                    game.print_board(board)
                    
                    result = game.is_game_finish(board)
                    if(result == 2):
                        print("\nDRAW\n")
                        break
                    if(result != 0): 
                        print("\nCan't Even Defeat a Robot???\n")
                        break
            
            elif(ch2 == 2):
                board = game.generate_new_board()
                game.print_board(board)
                while True:
                    print("\n", board)

                    nn.predict(game.get_board_state(board))
                    game.play_turn(board, 1, nn.best_move(board))
                    print()
                    game.print_board(board)
                    
                    result = game.is_game_finish(board)
                    if(result == 2):
                        print("\nDRAW\n")
                        break
                    if(result != 0): 
                        print("\nCan't Even Defeat a Robot???\n")
                        break

                    print()
                    print("\n Player 1")
                    while game.play_turn(board, -1, int(input("Enter Your Position: "))) == -1: pass
                    print()
                    game.print_board(board)

                    result = game.is_game_finish(board)
                    if(result == 2):
                        print("\nDRAW\n")
                        break
                    if(result != 0): 
                        print("\nYou WON\n")
                        break
            
            else: print("Invalid Choice")
        
        else: print("Invalid Choice")







if __name__ == "__main__":

    # Comprehensive Tic-Tac-Toe Training Data
    # Perspective: Player 1 (1 = our player, -1 = opponent, 0 = empty)
    # Output: Position to play (1-9, where 1=top-left, 9=bottom-right)

    test_data = data.comprehensive_test_data

    # Corresponding optimal moves (1-9 positions)
    output_data = data.comprehensive_output_data

    nn = NN(9, 9, 1, 9)

    # for i in range(9):
    #     print(nn.hidden_layers[0][i].weights, nn.output_layer[i].bias)
    learning_rate = 0.001
    for i in range(20000):
        # # Mini-batch training of size `batch_size`
        # batch_size = 32
        # indices = random.sample(range(len(test_data)), batch_size)
        # batch_inputs = [test_data[i] for i in indices]
        # batch_outputs = [output_data[i] for i in indices]
        # nn.train(batch_inputs, batch_outputs, learning_rate)

        nn.train(test_data, output_data, learning_rate)

        # print(nn.loss())
        # if i%100 == 0: print(nn.loss())
        # Decrease learning rate over time
        if i % 2000 == 0 and i > 0:
            learning_rate *= 0.95
        if i % 2000 == 0:
            print(f"Epoch {i}: Loss = {nn.loss():.4f}, LR = {learning_rate:.6f}")
            # nn.predict([1, 1, 0, -1, -1, 0, 0, 0, 0])
            # print([neuron.value for neuron in nn.output_layer])
            # print()

    print(nn.loss())
    print()
    nn.predict([1, 1, 0, -1, -1, 0, 0, 0, 0])
    print([neuron.value for neuron in nn.output_layer])

    

    # for i in range(9):
    #     print(nn.hidden_layers[0][i].weights, nn.output_layer[i].bias)
    



