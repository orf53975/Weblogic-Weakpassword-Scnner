# Weblogic-Weakpassword-Scnner
pip install requests

You can use masscan to scan ip range with CIDR format<br>
<pre>masscan -iL ip.txt -oL 7001.txt -p 7001 --max-rate=80000<br>
awk '{print $4,$3}' 7001.txt|sed 's/ /:/g' > scanned.txt
</pre>
1.python spider.py scanned.txt

2.python brute.py

Also can use with https://github.com/dc3l1ne/Weblogic_Automatical_Attacker to deploy war package automatically
