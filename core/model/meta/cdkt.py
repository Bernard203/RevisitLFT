import torch
from torch import nn

from .meta_model import MetaModel
from ..backbone.utils import convert_maml_module
from core.utils import accuracy

class CDKT(MetaModel):
    def __init__(self, model_func, n_way, n_support):
        super(CDKT, self).__init__()
        self.n_way = n_way
        self.n_support = n_support
        self.n_query = -1  # (change depends on input)
        self.feature = model_func()
        self.feat_dim = self.feature.final_feat_dim
        self.change_way = True

        self.device = 'cuda:0'
        ## GP parameters
        self.leghtscale_list = None
        self.noise_list = None
        self.outputscale_list = None
        self.iteration = 0
        self.writer = None
        self.feature_extractor = self.feature
        self.kernel_type = 'bncossim'
        self.get_model_likelihood_mll()  # Init model, likelihood

        self.normalize = True
        self.mu_q = []
        self.sigma_q = []

    def set_forward(self, batch):


    def set_forward_loss(self, batch):


    def set_forward_adaptation(self, support_set, support_target):
