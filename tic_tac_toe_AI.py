import neural_network

test_data = neural_network.data.comprehensive_test_data

# Corresponding optimal moves (1-9 positions)
output_data = neural_network.data.comprehensive_output_data

nn = neural_network.NN(9, 9, 1, 9)

# for i in range(9):
#     print(nn.hidden_layers[0][i].weights, nn.output_layer[i].bias)
learning_rate = 0.01
prev_loss = float('inf')
# 50,000 for best result with decay 0.97 lr=0.01 structure, 9->9->9
for i in range(50000): # Icreasing will not affect it
    # Mini-batch training of size `batch_size`
    # batch_size = 32
    # indices = neural_network.random.sample(range(len(test_data)), batch_size)
    # batch_inputs = [test_data[i] for i in indices]
    # batch_outputs = [output_data[i] for i in indices]
    # nn.train(batch_inputs, batch_outputs, learning_rate)

    # full data training
    nn.train(test_data, output_data, learning_rate)
    if nn.loss() < prev_loss:
        prev_loss = nn.loss()
    else:
        learning_rate *= 0.97

    # print(nn.loss())
    # if i%100 == 0: print(nn.loss())
    # Decrease learning rate over time
    # if i % 3000 == 0 and i > 0:
    #     learning_rate *= 0.95
    if i % 1000 == 0:
        print(f"Epoch {i}: Loss = {nn.loss():.4f}, LR = {learning_rate:.6f}")
        # nn.predict([1, 1, 0, -1, -1, 0, 0, 0, 0])
        # print([neuron.value for neuron in nn.output_layer])
        # print()

print(nn.loss())
print()
nn.predict([1, 1, 0, -1, -1, 0, 0, 0, 0])
print([neuron.value for neuron in nn.output_layer])



print()
neural_network.start_game_AI(nn)