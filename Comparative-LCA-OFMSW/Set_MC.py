# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:27:37 2022

@author: msardar2
"""
import numpy as np


def Set_MC(Treatment_processes, Collection_processes, common_data):
    Cost_LN_scale = 0.2
    Eqp_cost_scale = 0.2
    Eqp_elec_scale = 0.2
    Eqp_dsl_scale = 0.2
    
    #################### Landfill ####################
    if 'LF' in Treatment_processes:
        LF_Input = Treatment_processes['LF']['model'].InputData
        
        # Decay Rate
        LF_Input.LFG_param['actk']['uncertainty_type'] = 5
        LF_Input.LFG_param['actk']['loc'] = 0.04
        LF_Input.LFG_param['actk']['minimum'] = 0.02
        LF_Input.LFG_param['actk']['maximum'] = 0.17
        
        # Initial gas collection efficiency
        LF_Input.LFG_param['initColEff']['uncertainty_type'] = 3
        LF_Input.LFG_param['initColEff']['loc'] = 50
        LF_Input.LFG_param['initColEff']['scale'] = 5
        
        # Gas collection efficiency under intermediate cover
        LF_Input.LFG_param['intColEff']['uncertainty_type'] = 3
        LF_Input.LFG_param['intColEff']['loc'] = 75
        LF_Input.LFG_param['intColEff']['scale'] = 5
        
        # Increased gas collection efficiency 
        LF_Input.LFG_param['incColEff']['uncertainty_type'] = 3
        LF_Input.LFG_param['incColEff']['loc'] = 82.5
        LF_Input.LFG_param['incColEff']['scale'] = 3
        
        # Gas collection efficiency under final cover 
        LF_Input.LFG_param['finColEff']['uncertainty_type'] = 3
        LF_Input.LFG_param['finColEff']['loc'] = 90
        LF_Input.LFG_param['finColEff']['scale'] = 3
        LF_Input.LFG_param['finColEff']['maximum'] = 99
        
        # Combustion efficiency for electricity production  
        LF_Input.Energy_Rec['convEff']['uncertainty_type'] = 3
        LF_Input.Energy_Rec['convEff']['loc'] = 0.365
        LF_Input.Energy_Rec['convEff']['scale'] = 0.03
        
        # Landfill Operation time
        LF_Input.LF_Op['optime']['uncertainty_type'] = 2
        LF_Input.LF_Op['optime']['loc'] = 4.09
        LF_Input.LF_Op['optime']['scale'] = 0.6
        LF_Input.LF_Op['optime']['minimum'] = 10
        LF_Input.LF_Op['optime']['maximum'] = 200
        
        # Annual waste acceptance rate
        LF_Input.LF_Op['annWaste']['uncertainty_type'] = 4
        LF_Input.LF_Op['annWaste']['minimum'] = 100000
        LF_Input.LF_Op['annWaste']['maximum'] = 400000
        
        # Set Uncertainty for cost
        for k, v in LF_Input.Operational_Cost.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = Cost_LN_scale
        
    #################### WTE ####################
    if 'WTE' in Treatment_processes:
        WTE_Input = Treatment_processes['WTE']['model'].InputData
        
        # Combustion efficiency for electricity production 
        WTE_Input.Elec_Prod_Eff['Gross_Efficiency']['uncertainty_type'] = 3
        WTE_Input.Elec_Prod_Eff['Gross_Efficiency']['loc'] = 0.27
        WTE_Input.Elec_Prod_Eff['Gross_Efficiency']['scale'] = 0.03
        
        # Fraction of produced electricity used internally
        WTE_Input.Elec_Prod_Eff['Internal_use']['uncertainty_type'] = 3
        WTE_Input.Elec_Prod_Eff['Internal_use']['loc'] = 0.15
        WTE_Input.Elec_Prod_Eff['Internal_use']['scale'] = 0.02
        
        # Aluminum Recovery Rate from Bottom Ash (fraction)
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['uncertainty_type'] = 3
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['loc'] = 0.65
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['scale'] = 0.05
        
        
        # Ferrous Recovery Rate from Bottom Ash (fraction)
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['uncertainty_type'] = 3
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['loc'] = 0.9
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['scale'] = 0.05
        WTE_Input.Metals_Recovery['Al_Rec_Rate']['maximum'] = 0.95
        
        # Capital cost
        WTE_Input.Economic_parameters['Capital_cost']['uncertainty_type'] = 2
        WTE_Input.Economic_parameters['Capital_cost']['loc'] = np.log(
            WTE_Input.Economic_parameters['Capital_cost']['amount'])
        WTE_Input.Economic_parameters['Capital_cost']['scale'] = Cost_LN_scale
        
        # O&M cost except utility cost/income
        WTE_Input.Economic_parameters['O_M_cost']['uncertainty_type'] = 2
        WTE_Input.Economic_parameters['O_M_cost']['loc'] = np.log(
            WTE_Input.Economic_parameters['O_M_cost']['amount'])
        WTE_Input.Economic_parameters['O_M_cost']['scale'] = Cost_LN_scale
    
    #################### AD ####################
    if 'AD' in Treatment_processes:
        AD_Input = Treatment_processes['AD']['model'].InputData
        
        # Heat rate for electrical energy generation
        AD_Input.Biogas_gen['ad_HeatRate']['uncertainty_type'] = 3
        AD_Input.Biogas_gen['ad_HeatRate']['loc'] = 9.86
        AD_Input.Biogas_gen['ad_HeatRate']['scale'] = 0.4
        
        # Density of final compost
        AD_Input.Material_Properties['densFC']['uncertainty_type'] = 3
        AD_Input.Material_Properties['densFC']['loc'] = 700
        AD_Input.Material_Properties['densFC']['scale'] = 100
        
        
        # Capital Cost
        AD_Input.Economic_parameters['Unit_capital_cost']['uncertainty_type'] = 2
        AD_Input.Economic_parameters['Unit_capital_cost']['loc'] = np.log(
            AD_Input.Economic_parameters['Unit_capital_cost']['amount'])
        AD_Input.Economic_parameters['Unit_capital_cost']['scale'] = Cost_LN_scale
        
        # Set Uncertainty for cost
        for k, v in AD_Input.Operational_Cost.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = Cost_LN_scale
    
    #################### Composting ####################
    if 'Composting' in Treatment_processes:
        COMP_Input = Treatment_processes['Composting']['model'].InputData
        
        # Density of final compost
        COMP_Input.Material_Properties['densFC']['uncertainty_type'] = 3
        COMP_Input.Material_Properties['densFC']['loc'] = 700
        COMP_Input.Material_Properties['densFC']['scale'] = 100
        
        # Capital Cost
        COMP_Input.Economic_parameters['Unit_capital_cost']['uncertainty_type'] = 2
        COMP_Input.Economic_parameters['Unit_capital_cost']['loc'] = np.log(
            COMP_Input.Economic_parameters['Unit_capital_cost']['amount'])
        COMP_Input.Economic_parameters['Unit_capital_cost']['scale'] = Cost_LN_scale
        
        # Set Uncertainty for cost
        for k, v in COMP_Input.Operational_Cost.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = Cost_LN_scale

    #################### Home Composting ####################
    if 'HC' in Treatment_processes:
        HC_Input = Treatment_processes['HC']['model'].InputData
    
        # Density of final compost
        HC_Input.Material_Properties['densFC']['uncertainty_type'] = 3
        HC_Input.Material_Properties['densFC']['loc'] = 700
        HC_Input.Material_Properties['densFC']['scale'] = 100
    
        # Composter cost
        HC_Input.Economic_parameters['comp_cost']['uncertainty_type'] = 2
        HC_Input.Economic_parameters['comp_cost']['loc'] = np.log(
            HC_Input.Economic_parameters['comp_cost']['amount'])
        HC_Input.Economic_parameters['comp_cost']['scale'] = Cost_LN_scale

    #################### AnF ####################
    if 'AnF' in Treatment_processes:
        AnF_Input = Treatment_processes['AnF']['model'].InputData
        
        # Feed substitution factor (based on dry mass)
        AnF_Input.AnF_operation['FeedSubFac']['uncertainty_type'] = 4
        AnF_Input.AnF_operation['FeedSubFac']['minimum'] = 0.7
        AnF_Input.AnF_operation['FeedSubFac']['maximum'] = 1
        
        for k, v in AnF_Input.Input_dict.items():
            for c in ['Investment_cost', 'Installation_cost', 'O&M']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_cost_scale
            for c in ['motor']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_elec_scale           
            for c in ['diesel_use']:
                 if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_dsl_scale
    
    #################### RDF ####################
    if 'RDF' in Treatment_processes:
        RDF_Input = Treatment_processes['RDF']['model'].InputData
        
        for k, v in RDF_Input.Input_dict.items():
            for c in ['Investment_cost', 'Installation_cost', 'O&M']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_cost_scale
            for c in ['motor']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_elec_scale           
            for c in ['diesel_use']:
                 if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_dsl_scale
    
    #################### SS_MRF ####################
    if 'SS_MRF' in Treatment_processes:
        SS_MRF_Input = Treatment_processes['SS_MRF']['model'].InputData
        
        for k, v in SS_MRF_Input.Input_dict.items():
            for c in ['Investment_cost', 'Installation_cost', 'O&M']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_cost_scale
            for c in ['motor']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_elec_scale           
            for c in ['diesel_use']:
                if c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = Eqp_dsl_scale
    
    #################### GC ####################
    if 'GC' in Treatment_processes:
        GC_Input = Treatment_processes['GC']['model'].InputData
        
        # Electricity generation efficiency from High pressure steam
        GC_Input.Energy['elec_gen_eff_HP']['uncertainty_type'] = 3
        GC_Input.Energy['elec_gen_eff_HP']['loc'] = 0.34
        GC_Input.Energy['elec_gen_eff_HP']['scale'] = 0.03
        
        # Electricity generation efficiency from Medium pressure steam
        GC_Input.Energy['elec_gen_eff_MP']['uncertainty_type'] = 3
        GC_Input.Energy['elec_gen_eff_MP']['loc'] = 0.23
        GC_Input.Energy['elec_gen_eff_MP']['scale'] = 0.02
        
        # Fraction of RDF LHV used as electricity for syngas cleaning/internal uses
        GC_Input.Energy['frac_lhv_internal_elec']['uncertainty_type'] = 3
        GC_Input.Energy['frac_lhv_internal_elec']['loc'] = 0.0543
        GC_Input.Energy['frac_lhv_internal_elec']['scale'] = 0.01
        
        # Capital Cost
        GC_Input.Economic_params['capital_cost']['uncertainty_type'] = 2
        GC_Input.Economic_params['capital_cost']['loc'] = np.log(
            GC_Input.Economic_params['capital_cost']['amount'])
        GC_Input.Economic_params['capital_cost']['scale'] = Cost_LN_scale
    
        # operational cost except utility cost/income
        GC_Input.Economic_params['O&M_cost']['uncertainty_type'] = 2
        GC_Input.Economic_params['O&M_cost']['loc'] = np.log(
            GC_Input.Economic_params['O&M_cost']['amount'])
        GC_Input.Economic_params['O&M_cost']['scale'] = Cost_LN_scale
    
    
    #################### Reprocessing ####################
    if 'Reprocessing' in Treatment_processes:
        Reproc_Input = Treatment_processes['Reprocessing']['model'].InputData
        
        for k, v in Reproc_Input.Input_dict.items():
            for c in [('Technosphere', 'Electricity_production'),
                      ('Technosphere', 'Electricity_consumption')]:
                if  c in v.keys():
                    if v[c]['amount'] > 0:
                        v[c]['uncertainty_type'] = 2
                        v[c]['loc'] = np.log(v[c]['amount'])
                        v[c]['scale'] = 0.2
                    
    #################### CommonData ####################
    
    # Nitrogen mineral fertilizer equivalent
    common_data.Land_app['MFEN']['uncertainty_type'] = 4
    common_data.Land_app['MFEN']['minimum'] = 0.2
    common_data.Land_app['MFEN']['maximum'] = 0.8
    
    # Phosphorus mineral fertilizer equivalent
    common_data.Land_app['MFEP']['uncertainty_type'] = 4
    common_data.Land_app['MFEP']['minimum'] = 0.8
    common_data.Land_app['MFEP']['maximum'] = 1
    
    # Potassium mineral fertilizer equivalent
    common_data.Land_app['MFEK']['uncertainty_type'] = 4
    common_data.Land_app['MFEK']['minimum'] = 0.8
    common_data.Land_app['MFEK']['maximum'] = 1
    
    # Percent of carbon in compost remaining after 100 years
    common_data.Land_app['MFEK']['uncertainty_type'] = 4
    common_data.Land_app['MFEK']['minimum'] = 0.02
    common_data.Land_app['MFEK']['maximum'] = 0.16
    
    # Percent of applied N evaporated as N2O
    common_data.Land_app['perN2Oevap']['uncertainty_type'] = 4
    common_data.Land_app['perN2Oevap']['minimum'] = 0.013
    common_data.Land_app['perN2Oevap']['maximum'] = 0.022
    
    # Volumetric peat replacement factor
    common_data.Land_app['PeatSubFac']['uncertainty_type'] = 5
    common_data.Land_app['PeatSubFac']['loc'] = 1
    common_data.Land_app['PeatSubFac']['minimum'] = 0.9
    common_data.Land_app['PeatSubFac']['maximum'] = 1.1
    
    #################### SF Collection ####################
    if 'SF' in Collection_processes:
        SF_Input = Collection_processes['SF']['model'].InputData
        
        # Travel speed
        for k, v in SF_Input.Speed.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Loading time at one service stop
        for k, v in SF_Input.TL.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Time to unload at disposal facility
        for k, v in SF_Input.S.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Cost (a=Fringe benefit rate, d=Other expenses rate, e=Administrative rate, Wa=Hourly wage for a collector)
        # Cost (Wd=Hourly wage for a driver, Pt=Unit price of a vehicle, c=Vehicle operation and maint. Cost, Pb=Unit price of a bin)
        for k in ['a', 'd', 'e', 'Pt', 'c', 'Wd', 'Wa', 'Pb']:
            if SF_Input.LCC[k]['amount'] > 0:
                SF_Input.LCC[k]['uncertainty_type'] = 2
                SF_Input.LCC[k]['loc'] = np.log(SF_Input.LCC[k]['amount'])
                SF_Input.LCC[k]['scale'] = 0.2
    
    #################### MF Collection ####################
    if 'MF' in Collection_processes:
        MF_Input = Collection_processes['MF']['model'].InputData
        
        # Travel speed
        for k, v in MF_Input.Speed.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Loading time at one service stop
        for k, v in MF_Input.TL.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Time to unload at disposal facility
        for k, v in MF_Input.S.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Cost (a=Fringe benefit rate, d=Other expenses rate, e=Administrative rate, Wa=Hourly wage for a collector)
        # Cost (Wd=Hourly wage for a driver, Pt=Unit price of a vehicle, c=Vehicle operation and maint. Cost, Pb=Unit price of a bin)
        for k in ['a', 'd', 'e', 'Pt', 'c', 'Wd', 'Wa', 'Pb']:
            if MF_Input.LCC[k]['amount'] > 0:
                MF_Input.LCC[k]['uncertainty_type'] = 2
                MF_Input.LCC[k]['loc'] = np.log(MF_Input.LCC[k]['amount'])
                MF_Input.LCC[k]['scale'] = 0.2
                
    #################### COM Collection ####################
    if 'COM' in Collection_processes:
        COM_Input = Collection_processes['COM']['model'].InputData
        
        # Travel speed
        for k, v in COM_Input.Speed.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Loading time at one service stop
        for k, v in COM_Input.TL.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Time to unload at disposal facility
        for k, v in COM_Input.S.items():
            if v['amount'] > 0:
                v['uncertainty_type'] = 2
                v['loc'] = np.log(v['amount'])
                v['scale'] = 0.2
        
        # Cost (a=Fringe benefit rate, d=Other expenses rate, e=Administrative rate, Wa=Hourly wage for a collector)
        # Cost (Wd=Hourly wage for a driver, Pt=Unit price of a vehicle, c=Vehicle operation and maint. Cost, Pb=Unit price of a bin)
        for k in ['a', 'd', 'e', 'Pt', 'c', 'Wd', 'Wa', 'Pb']:
            if COM_Input.LCC[k]['amount'] > 0:
                COM_Input.LCC[k]['uncertainty_type'] = 2
                COM_Input.LCC[k]['loc'] = np.log(COM_Input.LCC[k]['amount'])
                COM_Input.LCC[k]['scale'] = 0.2
