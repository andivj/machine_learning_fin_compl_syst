#HMM python script and datasets#
The datasets are all built using the same parameters from the paper of professor Fantulin. 
NOTE: the states in the Markov chain are persistent so it is difficult for it to change hidden state. 
The name of the dataset contains the length of the time series. Every dataset contains 1000 simulations as in the paper. Each column has a name and a number that inform on what the column describes: 
1. return is a column of values;
2. states is the column of hidden states (so we can evaluate BAC);
3. the number associated with each column has to be used to connect the corresponding columns. 