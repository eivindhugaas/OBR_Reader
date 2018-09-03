import matplotlib.pyplot as plt
threshold=500.

Strain=[-55.1781693, -55.192688, -59.4237671, -50.990654, -55.1968384, -50.9533195, -46.7409134, -29.760622, -38.2269173, -21.2258835, -8.47666454, -16.9740696, -8.50155354, -12.7741079, 
        -16.9616261, -4.29536915, -25.4859943, -25.4528084, -17.0217724, -12.7347002, -29.7191429, -25.4694004, -21.205143, -25.4673271, -21.2258835, -25.5357704, -21.2694397, -29.7544003, 
        -25.4569569, -25.4486618, -29.7066975, -34.0124359, -29.7315826, -29.7232876, -29.7253647, -29.6901035, -29.727438, -33.979248, -29.727438, -33.9419174, -29.7295113, -25.4942894, 
        -29.7772141, -42.5139885, -25.4942894, -42.5139885, -46.7429886, -42.4828758, -59.4341316, -63.7378006, -67.9377594, -84.9761276, -76.4704208, -72.2538681, -89.2134247, -93.4216766, 
        -76.48909, -84.9118271, -76.4787216, -51.0072441, -46.7222481, -29.7502499, -29.7087708, -25.4590302, -21.2155132, -42.5036163, -21.2632179, -8.47044277, -16.9906635, -12.7201824, 
        -0.0228146091, -0.0477032736, -16.9388103, -21.246624, -12.7326269, -25.5171032, -33.9522858, -33.9585114, -50.9222069, -51.0010223, -46.7388382, -46.6807671, -42.4455452, -33.9751053, 
        -34.0165825, -38.1978798, -29.6921787, -46.6849136, -42.4393234, -38.2870636, -42.4973946, -50.9470978, -34.0103607, -42.4248047, -29.6880302, -29.7668457, -38.2289886, -29.7004757,
        -21.2549191, -21.3005505, -21.2486973, -25.4756241, -25.4528084, -21.2321053, 0.0477032736, -12.6911459, -12.7056637, -21.2362537, -4.2767024, -8.4870348, -0.00622216659, -21.230032, 
        -16.9554043, -21.2445507, -8.48496056, -25.4714756, -0.0580735542, -4.26840591, -21.2009945, -0.0186664984, -4.24559164, 8.47666454, 17.0051804, 4.2435174, 12.7264042, 8.5202198, 
        21.2611427, 8.4870348, -4.21862888, 21.205143, 4.24144316, -8.49533176, -8.51399803, -4.27462816, -17.0155506, -29.7398815, -8.5326643, -8.48081303, -8.46629429, -16.9802914, 
        -4.28292465, -33.9771767, -12.7927742, -33.9543648, -17.0279961, -21.2528477, -29.7232876, -21.2341805, -38.1978798, -21.2113647, -17.0134754, -25.5254002, -33.9771767, -16.9678478, 
        -16.9429588, -29.760622, -29.7647686, -33.9522858, -12.7575159, -38.2746201, -38.249733, -25.5150318, -8.50777531, -12.7595892, -29.6901035, -29.7689171, -12.7388487, -42.4704323, 
        -33.9813271, -50.9699135, 0.0456292182, -29.7315826, -33.9896202, -25.4901409, -38.2020264, -21.2175865, -46.7388382, -12.7533665, -21.2549191, -29.7046204, -29.727438, -33.9647331, 
        -46.7346916, -42.4911728, -29.7149925, -12.7512932, -46.7243195, -46.7326164, -76.4766464, -12.7409229, -34.0062141, -33.9522858, -55.2300224, -29.7253647, -42.493248, -42.451767, 
        -38.2269173, -25.4901409, 4.25596189, -17.0383663, -33.9979172, -33.9771767, -21.2632179, -42.5077667, -25.4818459, 16.9761429, -16.9637012, -8.60940456, -25.4901409, -21.2445507, 
        -59.4859848, -8.4745903, -38.2165489, -8.50570202, -50.9512482, 25.5129566, -67.9460526, -12.8031445, -25.5088081, -55.2092857, -17.011404, 4.29951715, -8.54510784, -12.7699594,
        4.22070265, -25.4673271, -50.9802818, -1648.10669, -7161.61035, -80.7139359, -12.7575159, -2378.66553, -46.7409134, -84.9761276, 38.2352104, -25.5171032, -33.9854736, -42.4973946, 
        -29.7544003, -50.9885788, -42.4538422, -8.54096031, -93.4320526, -38.1875076, -1333.76489, -55.2113571, -25.5005112, 5309.54785, -63.6880188, 16.9989586, -21.1989193, 0.0331848897, 
        -2739.74219, -17.0404396, -25.4797707, -0.0456292182, -33.9999886, -46.7326164, -46.7035828, -84.9553833, -8.63014412, -29.7232876, -21.2652893, -29.7149925, 0.167998493, -0.0497773327, 
        -93.4092331, -38.2289886, -17.0072556, -21.2258835, -42.3957672, 0.0539254397, 46.7326164, 17.0196991, 46.6994324, -1350.73279, 17.0051804, -0.116147108, -8.51607132, -3045.58862, 
        -0.130665496, 0.201183379, 29.7191429, -7072.37939, 72.1989059, 0.118221156, 21.2404022, -4.49447823, -0.0248886663, -29.7129192, 0.0207405537, -0.377478093, 6549.87646, 0.0891843885,
        12.7824039, 76.4455338, -1541.86731, -0.367107809, 4175.44287, 1053.4408, 4655.45801, 4515.27148, 1371.99817, 6320.53857, -8469.84863, -4141.48438, -1609.82385, -756.05957, 7463.13818,
        645.652405, -815.506165, -2238.49097, 3215.47559, 4570.49268, -2574.08545, 1520.63318, 3088.07471, -148.630966, 3602.01025, 203.883804, -352.583191, -1469.67981, -679.616089, 1261.55872,
        7985.62598, -768.835754, -590.417175, 3245.23413, 1138.34229, 887.778687, -424.749969, -594.712585, -641.403687, -802.810852, 790.066833, -365.299255, -369.546906, -365.295105, 
        -1512.19165, -547.932251, 3215.48071, -59.4735374, -25.5025864, -7917.61133, 0.271701276, -0.732141554, -0.120295219, 0.201183379, -0.0559994988, -0.111998998, -5126.95557, -0.447995991,
        -33.995842, 930.19519, 2599.63135, 89.1688309, 17.0528831, -8516.56934, -3453.32495, 3453.33228, 2149.32397, -671.139465, 10975.9854, 12607.0674, 8304.18555, -1278.54517, -10517.2197, 
        -6558.41211, -11549.4082, -2748.2168, -581.932251, -5730.10107, -0.261330992, 297.346954, -0.77984488, -0.501921415, -0.350515366, 4256.1748, 3160.26929, -1609.86304, 7989.85059, 
        -0.744585872, 0.335996985, -0.686512351, 0.790215135, -21.2134399, -841.044006, 6749.49414, -0.402366757, 4702.19238, -0.518513858, 2285.25635, 1397.49133, 985.466736, -5275.60254, 
        310.076477, 1465.44043, -4.46958971, -4778.61523, -378.03186, -7870.9248, -63.7087631, -1176.59509, 904.758911, -344.052612, -7369.68701, -0.186664984, 6724.03174, 3194.24121, 
        135.913895, -1287.03027, -395.072296, -322.81015, -59.479763, -1231.8501, 0.182516873, 0.516439795, 4570.4873, 8928.58301, 1270.07996, 1826.44543, -8057.80859, 2344.74048, 2879.95679, 
        6532.94043, 322.864075, -348.318939, -2450.89258, -2089.86182, -845.297913, -1741.52014, 1083.14221, -220.880692, 1992.14282, 0.23436828, 0.354663491, -0.0767400563, 0.535106301, 
        -0.0954065472, 0.356737554, -0.0228146091, 0.0808881596, -0.109924942, 0.107850879, -0.0207405537, 0.207405537, -0.167998493, 0.197035268, -0.269627213, 0.0746659935, 0.0435551666, 
        0.0518513843, -0.00829622243, -0.143109828, 0.184590936, 0.130665496, -0.335996985, -0.0705178827, 0.0435551666, 0.0891843885, 0.0477032736, 0.0456292182, -0.33184886, 0.543402553, 
        -0.134813607, -0.0394070558, -0.205331489, 0.0642957166, 0.0933324918, -0.153480113, 0.0290367771, -0.0269627199, 0.176294714, 0.0663697794, 0.0539254397, -0.186664984, 0.0642957166,
        -0.105776832, 0.226072043, -0.228146091, 0.114073046, 0.221923947, -0.103702769, -0.0559994988, -0.0788141116, -0.0746659935, 0.141035765, 0.0145183885, 0.0622216612, 0.101628713, 
        0.0186664984, -0.16592443, 0.178368777, -0.0394070558, -0.130665496, 0.0580735542, 0.180442825, -0.0352589414, -0.400292724, 0.2094796, 0.0165924449]
#SmoothStrain=[]
#for i in range(len(Strain)):
   #lastm=Strain[0]
   #nextm=Strain[0]   
   #m=Strain[i]
   #if i==len(Strain)-1:
      #nextm=Strain[-1]   
   #else:
      #lastm=Strain[i-1]
      #nextm=Strain[i+1]
   
   #if m>threshold+lastm and m>threshold+nextm:
      #msmooth=(lastm+nextm)/2.
   #elif m<-threshold+lastm and m<-threshold+nextm:
      #msmooth=(lastm+nextm)/2.
   #else:
      #msmooth=Strain[i]
  
   #SmoothStrain.append(msmooth)   

#plt.plot(Strain)
#plt.ylabel('some numbers')
#plt.plot(SmoothStrain)
#plt.show()

Diff=[]
      
for i in range(len(Strain)): 
   m=Strain[i]
   if i==0:
      lastm=Strain[0]   
   else:
      lastm=Strain[i-1]   
   Diffi=m-lastm
   Diff.append(Diffi)   
   
smoothn=[]
for i in range(len(Diff)):
   if abs(Diff[i])>1000:
      n=0.
   else:
      n=1.
   smoothn.append(n)

print(smoothn)
smoothslist=[]
for i in range(len(smoothn)):
   currentsmoothn=smoothn[i]
   lastsmoothn=1.0
   nextsmoothn=1.0  
   if i>0 and i<len(smoothn)-1:
      print(i)
      currentsmoothn=smoothn[i]
      lastsmoothn=smoothn[i-1]
      nextsmoothn=smoothn[i+1]
   if currentsmoothn==0.0 and lastsmoothn==0.0:
      if nextsmoothn==1.0:
         smooths=1.0
   else:
      smooths=currentsmoothn
   smoothslist.append(smooths)
   

   
StrainCut=[]   
for i in range(len(smoothn)):
   StrainS=Strain[i]*smoothslist[i]
   StrainCut.append(StrainS)
   
for i in range(len(smoothn)):
   if smoothn[i]==0.0:
      n=n+1
      avg=1.0/(n+1)
   elif smoothn[i]==1.0:
      n=0
   
   StrainS=Strain[i]*smoothslist[i]
   StrainCut.append(StrainS)

print(smoothn)
print(smoothslist)

   
plt.plot(StrainCut)
plt.plot(Strain)

plt.show()
      