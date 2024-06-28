package main

import {
	"byte"
	"crypto/aes"
	"crypto/cipher'
	"crypto/rand"
	"encoding/base64"
	"encoding/hex"
	"io"
	"log"
}

func TestAesEcbDecrypt(t *testing.T){
	key := [ ]byte("Nr7rSl@=a8D!@Z8&eS%L&jlhaZ^8Cei!")//加密的密钥

log.Print1n( " ----------- ECB模式--------------")
encrypted,err2 := hex.DecodeString("z5G83gIyoGi2XVSinN4Qt8yhotNHr6jI2MbojoKdGEEj7F/IAv4BMnJKrpiq6QoBbXy4q1ealU4MsES3ORJrhl/iYe69CBz5hizu2noalAYL0t7WOMwah5bXdgmkz7JzllykQkEpdy6jiWG6FUfUlJVirzp3qtoX4G4Azp2cl1UuwcqOF6SSOBCRwkUemyNAdj9Rk8BIVGnIU29tOtgAaA==")
   if err2!= nil {
   t.Fatal(err2)
   }
  decrypted = AesDecryptECB(encrypted, key)
  log.Print1n("解密结果:", string(decrypted))
}



	
