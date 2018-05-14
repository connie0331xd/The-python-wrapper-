
# coding: utf-8

# In[1]:


import sys,os


# In[3]:


def reformat_datetime(dt) :
    fields = dt.split(' ')
    print (fields[0])
    y, m, d = fields[0].split('/')
    t = fields[1] + ':00'
    return y + '-' + m + '-' + d + ' ' + t 


# In[87]:


# Make a table a list as below
dict={"1":"A_Env","2":"A_PVD","3":"A_Bnv","4":"A_Cnv","5":"A_dnv","6":"A_env","7":"A_fnv",
          "8":"A_gnv","9":"A_hnv","10":"A_inv","11":"A_jnv","12":"A_knv","13":"B_lnv","14":"B_mnv",
          "15":"B_nnv","16":"B_onv","17":"B_pnv","18":"B_qnv","19":"B_rnv","20":"B_snv","21":"B_tnv",
          "22":"B_unv","23":"B_vnv","24":"B_wnv","25":"C_xnv","26":"C_ynv","27":"C_znv","28":"C_aa",
          "29":"C_bb","30":"C_cc","31":"C_dd","32":"C_ee","33":"C_hh"}

with open(sys.argv[1], 'rt') as f :
    lines = f.readlines()
    for line in lines [1:] :
        fields = line.split(',')
        dt_real = reformat_datetime(fields[0])
        new_id = dict[fields[1].strip()]
        print('%s,%f,%s,%s' % (dt_real,float(field[3]),'F11_' + new_id,'NH3'))

