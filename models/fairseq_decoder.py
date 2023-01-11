
import torch.nn as nn
import torch.nn.functional as F


class FairseqDecoder(nn.Module):
    """Base class for decoders."""

    def __init__(self, dictionary):
        super().__init__()
        self.dictionary = dictionary

    def forward(self, prev_output_tokens, encoder_out):
        raise NotImplementedError

    def get_normalized_probs(self, net_output, log_probs, _):
        """Get normalized probabilities (or log probs) from a net's output."""
        logits = net_output[0].float()
        if log_probs:
            return F.log_softmax(logits, dim=-1)
        else:
            return F.softmax(logits, dim=-1)

    def max_positions(self):
        """Maximum input length supported by the decoder."""
        raise NotImplementedError

    def upgrade_state_dict(self, state_dict):
        return state_dict
