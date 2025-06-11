Network Intrusion
A network intrusion has been detected! Security analysts captured network traffic during the incident, but they need your help to analyze what happened.


found some exfiltration text using strings *.pcap. then base64 decoded.

---

Evidence Disk
A disk image has been captured from the suspect's machine. Your task is to find the hidden flag

direct with photorec

---

Weak RSA
The larger the primes used in rsa, the stronger it is.

factored n using https://www.alpertron.com.ar/ECM.HTM
then wrote code to find d, and then the original message

---

Fair Enough
Wrap the result in dcCTF{} and submit. The encrypted message is:
ERQDUBDTZUQFDOMHLFGT

went to https://www.dcode.fr/playfair-cipher and did dictionary attack

---

XOR
I encypted this message via a very strong function, Its so strong I don't even have to remember a long key!

17022d30351a0a541d35313640110b25073e1654211c
View Hint: Hint
You know what the plain text should begin with...

found 'sand' as key after xoring first 6. then took xor for all.

---

Oui Oui Secret
A cryptographer's secret has been discovered. But alas he died and could not tell us the key.

The intercepted transmission contains:

geMRX{sry_ngv_jrw_lpmehhypup_wjsq}

went to https://www.dcode.fr/vigenere-cipher and used partial key feature, where partial key was found using first 5 letters

---

Classic Caesar
The ancient Roman general has returned with a new message. His cipher technique hasn't changed much over the centuries.

Decode the message to find the flag!

gfFWI{FDHVDU_QHYHU_GLHV}

straightforward

---

Hidden in Plain Sight
100
A seemingly innocent image contains a secret message.

View Hint: Hint?
stegseek has some modes of running

View Hint: Hint?
you can run stegseek with rockyou.txt to bruteforce the passphrase


2nd hint is it

---

Chameleon Image
100
An image has been discovered that appears to be more than meets the eye.

View Hint: Hint?
Use binwalk or foremost or similar tools

direct binwalk

---

Sound of Secrets
Listen carefully to this mysterious audio file... or should you? Can you find the true message hidden within?

When you find the message, wrap it in dcCTF{} to submit as the flag.

generated spectrogram using https://convert.ing-now.com/audio-spectrogram-creator/
saw morse code on the top

---

