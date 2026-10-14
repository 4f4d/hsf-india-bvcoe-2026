#!/usr/bin/env python

import os
# some more imports



# MVA VARIABLES
mvaVariables = [
"Electron_charge",
"Electron_eta",
"Electron_mass",
"Electron_mvaFall17V2Iso_WP90",
"Electron_phi",
"Electron_pt",
"Jet_btagDeepFlavB",
"Jet_eta",
"Jet_jetId",
"Jet_mass",
"Jet_phi",
"Jet_pt",
"Jet_puId",
"Muon_charge",
"Muon_eta",
"Muon_mass",
"Muon_pfRelIso04_all",
"Muon_phi",
"Muon_pt",
"Muon_tightId",
"PuppiMET_phi",
"PuppiMET_pt"
"dphill",
"mjj",
"mll",
"mth",
"mtw2",
"nJet",
"ptll"
]


PROCESS_SAMPLES = ["DY_train", "ZH_HToGluGlu_ZToLL-M125"]

# # TRAIN / TEST SAMPLE DEFINITIONS
# TRAIN_SAMPLES = [
#     # 'Hgluglu',
#     # 'qqZHgluglu',
#     # 'ggZHgluglu',
#     'DY_train',
#     'ZH_HToGluGlu_ZToLL-M125'
# ]

# TEST_SAMPLES = [
#     'ZH_HToGluGlu_ZToLL-M125',
#     # 'DY_test'
#     # 'Hgluglu',
#     # 'qqZHgluglu',
#     # 'ggZHgluglu',
#     'DY_train'
# ]




# XGBOOST CONFIGURATIONS

XGB_CONFIGS = {
    "xgb_d5_lr03_n700_dense": {"n_estimators": 700, "max_depth": 5, "learning_rate": 0.03, "subsample": 0.85, "colsample_bytree": 0.75,
                                "min_child_weight": 5, "reg_lambda": 2.0, "gamma": 0.5
    },

    # "xgb_d6_lr03_n600_l2": {"n_estimators": 600, "max_depth": 6, "learning_rate": 0.03, "subsample": 0.8, "colsample_bytree": 0.7,
    #                          "min_child_weight": 8,"reg_lambda": 3.0, "gamma": 1.5
    # },

    # "xgb_d6_lr03_n700_l1l2": { "n_estimators": 700, "max_depth": 6, "learning_rate": 0.03, "subsample": 0.8, "colsample_bytree": 0.7,
    #                            "min_child_weight": 10, "reg_alpha": 0.5, "reg_lambda": 2.0, "gamma": 1.0
    # },

}

# MAIN
def train_bdt():

    # write your script here to train the BDT using the configurations and variables defined above
    # You should have plots for training and testing, and save the trained model to a file 

if __name__ == "__main__":
    runJob()