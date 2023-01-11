<h1 align="center">  
End-to-end Attention-based MLCNN-LSTM Hybrid Model for Grammatical Error Correction (GEC) system by extending the Facebook’s AI Sequence Modelling toolkit (Faiqseq) </h1>
<p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211837536-ee33fa5b-609c-42b7-8a87-4ebd17d046e4.png">
</p>

# Install

### Clone the repository:

          git clone https://github.com/Lizahh/Attention-based-MLCNN-LSTM-Hybrid-Model-for-GEC

### Install the requiements:
  
          pip3 install -r requirements.txt

# Description:

* Presents a sequence to sequence network with an encoder neural network that interprets and encodes source sentences into a fixed-length vector, and a decoder that produces output as a corrected sentence from the continuous spaced encoded vector
* The encoder-decoder network is trained conjointly to exploit the likelihood of a correct output
* Uses a Multi-Layer Convolutional Neural Network in the encoder to make the network more parallelizable and extract features over larger context of size ‘N’ with kernel width of ‘k’
* Decoder is an attention-based long short-term memory (LSTM) network to address the issue of long-term dependencies 
* The joint network of encoder-decoder is applied to the ConLL-2014 shared task for Grammatical Error Correction (GEC) system
* Comparison and evaluation techniques are presented for GEC system

# Usage:

* Illustration of a simple character-based encoder-decoder neural network model that has one encoder hidden layer and one decoder layer, being trained jointly is shown below. The wrong-spelled word ‘LEVL’ is fragmented into characters and is converted into an embedded vector. This projected vector is remitted towards the decoder to correct the word as ‘LEVEL’.
  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211836244-e8a381ba-2f39-4e35-8609-6d46ce9fef93.png">
</p>

* Multilayer Convolutional Neural Network (CNN) architecture for text encoding to use in Grammatical Error Correction (GEC) system is shwon below. (Bottom to Top) Here, text sentence of size s and dimension d is depicted in which 3-sized window size is used for the kernel to generate 2h feature maps. Then, a Gated Linear Unit (GLU) with residual connection is applied, in which two consecutive blocks are chosen and the first one is element-wise multiplied with the sigmoid of the other and then the residuals are added to the output. In the end, a pooled layer is applied on all feature maps that are afterward used as input to the subsequent layer of encoder.
  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211836786-2d6d9547-e953-4f7a-b3ef-e315e54af930.png">
</p>

* Unification of the eventual flattened encoded output of Multi-Layer Convolutional Neural Network X(s) to Long Short-Term Memory Network to predict the target word Y and hidden state h(t) with the previous hidden states and previous hidden cells (where 𝐶𝑡 shows the produced cell state from previous cell state 𝐶𝑡−1 and combination of forget (𝑓𝑡), input (𝑖𝑡) and output gate (𝑜𝑡) at t time step)

  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211837233-950cb99d-77d6-49b6-a0b8-0cf316bbc15b.png">
</p>

# Results:

* The computation of the perplexity epochs during training that signifies the divergence of the data:
  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211838535-77c1cac1-d725-4bdd-930c-855b976b187f.png">
</p>

* PERFORMANCE OF VARIOUS ARCHITECTURES:
  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211838762-4867d674-6daa-45a7-9877-b51c63db3dcd.png">
</p>

* Depiction of the cross entropy cost function for training and validation datasets:
  <p align="center" width="80%">
    <img src="https://user-images.githubusercontent.com/44564025/211838948-7134044f-e406-4c3c-a6fb-16be66e42457.png">
</p>

# You might be interested:

* [GUI based Integrated LMS desinged with PyQt5](https://github.com/Lizahh/GUI-based-Integrated-LMS-desinged-with-PyQt5)
* [OPAC (Online Public Access Catalog) Library Management Project with Pure Python](https://github.com/Lizahh/Simplest-Library-Management-System-using-Python-Only)


