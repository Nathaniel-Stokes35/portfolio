import math
import os
import pandas as pd
pi = math.pi

def main():
    cans = []
    can_names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    rad_can = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    hei_can = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    best_ce = 0
    best_se = 0

    for can in range(len(rad_can)):
        se = cal_store_eff(rad_can[can], hei_can[can])
        vol = cal_volume(rad_can[can], hei_can[can])
        ce = cal_cost_eff(vol, cost[can])
        cans.append({'Name':can_names[can], 'Radius':rad_can[can], 'Height':hei_can[can], 'Cost':cost[can], 'Volume':vol, 'Cost-Effeciency':ce, 'Store-Effeciency':se})
        if ce > best_ce:
            best_ce = ce
            best_ce_can = can
        if se > best_se:
            best_se = se
            best_se_can = can
        print(f'{can} Store-Effeciency: {se}{os.linesep}\tCost-Effeciency: {ce}')
    can_df = pd.DataFrame(cans)
    print(can_df)
    print(f'Best Store Effecent Can: {cans[best_se_can]}.{os.linesep}Best Cost Effecent Can: {cans[best_ce_can]}.')

def cal_volume(rad, hei):
    return(pi*rad**2*hei)
def cal_sa (rad, hei):
    return(2*pi*rad*(rad+hei))
def cal_store_eff(rad, hei):
    vol = cal_volume(rad, hei)
    sa = cal_sa(rad, hei)
    return(vol/sa)
def cal_cost_eff (vol, cost):
    return(vol/cost)

main()