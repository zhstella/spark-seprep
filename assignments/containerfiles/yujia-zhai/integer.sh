INTEGER=$(curl -sS 
https://www.random.org/integers/?num=100&min=1&max=100&col=5&base=10&format=html&rnd=new | tail -n 1) #this file contains an integer and the comment explains that
echo "$INTEGER"
echo
exit 0
