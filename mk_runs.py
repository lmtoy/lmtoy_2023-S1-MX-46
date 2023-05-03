#! /usr/bin/env python
#
#

import os
import sys

from lmtoy import runs

project="2023-S1-MX-46"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['G09-44907'] = [ 104042, 104043, 104044, 104046, 104047,     # jan 26
                    104048, 104050, 104051, 104052, 104055,
                    104056, 104057, 104059, 104060, 104061,
                    104063, 104064, 104065,
                    104143, 104144, 104145, 104147, 104148,     # jan 27
                    104149, 104151, 104152, 104153, 104168,
                    104169, 104170, 104172, 104173, 104174,
                    104176, 104177, 104178,
                    104665]                                     # feb 5
                   
on['G12-42911'] = [ 104100,-104101, 104102, 104104,-104105, 104106,    # jan 26
                    104225, 104226, 104227, 104229, 104230, 104231,    # jan 27
                    104401, 104402, 104403,                            # jan 31 (power failure)
                    104459, 104460, 104461, 104463, 104464, 104465,
                    104467, 104468, 104469, 104487, 104488, 104489,
                    104491, 104492, 104493, 104495, 104496, 104497,
                    104500, 104501, 104502]                            # feb 2

on["NGP-115876"] = [ 104582, 104583, 104584, 104586, 104587, 104588,
                     104590, 104591, 104592, 104595, 104596, 104597,
                     104599, 104600, 104601, 104603, 104604, 104605,
                     104608, 104609, 104610, 104612, 104613, 104614,
                     104616, 104617, 104618,
                     104711, 104712, 104713, 104715, 104716, 104717,
                     104719, 104720, 104721]                           # feb 5

 
on["NGP-131281"] = [ 104621, 104622, 104623, 104625, 104626, 104627,
                     104629, 104630, 104631, 104634, 104635, 104636,
                     104638, 104639, 104640,
                     104950, 104951, 104952, 104954, 104955, 104956,
                     104958, 104959, 104960, 104962, 104963, 104964,
                             104995, 104996, 104997, 104999, 105000,
                     105001, 105003, 105004, 105005,                   # feb 8
                     105091, 105092, 105093,]                          # feb 9


on['NGP-78659']  = [ 104506, 104507, 104508,                            # feb 2
                     104852, 104853, 104854, 104856, 104857, 104858,
                     104860, 104861, 104862,                            # feb 6
                     105009, 105010, 105011, 105013, 105014, 105015,
                     105018, 105019, 105020,                            # feb 8
                     105097, 105098, 105099, 105101, 105102, 105103,
                     105105, 105106, 105107, 105110, 105111, 105112,
                     105114, 105115, 105116,]                           # feb 9

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['G09-44907']   = "speczoom=78,3"
pars1['G12-42911']   = "speczoom=93,4 badcb=0/2,2/2"
pars1["NGP-115876"]  = "speczoom=89,3"
pars1["NGP-131281"]  = "speczoom=89,3"
pars1['NGP-78659']   = "speczoom=78,3 badcb=0/2,3/3,3/4"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['G09-44907']   = "srdp=1 admit=0"
pars2['G12-42911']   = "srdp=1 admit=0"
pars2["NGP-115876"]  = "srdp=1 admit=0"
pars2["NGP-131281"]  = "srdp=1 admit=0"
pars2['NGP-78659']   = "srdp=1 admit=0"

if __name__ == '__main__':
    runs.mk_runs(project, on, pars1, pars2)
