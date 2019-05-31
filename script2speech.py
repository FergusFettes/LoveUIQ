voices = [
 'nitech_us_rms_arctic_hts',
 'nitech_us_slt_arctic_hts',
 'nitech_us_awb_arctic_hts',
 'cmu_us_slt_cg',
 'cmu_us_awb_cg',
 'cmu_us_rms_cg',
]

with open('opening.txt', 'r') as op:
    lines = op.readlines()

voice=None
script=[]
for l in lines:
    if l=="PILOT\n":
        voice = voices[1]
    elif l=="FRED\n":
        voice = voices[0]
    else:
        script.append("(voice_{})".format(voice))
        script.append('(SayText "{}")'.format(l[:-1]))

with open('script.scm', 'w') as fi:
    for li in script:
        fi.write(li)
