import java.io.*;
import java.security.*;

public class GenerateDigitalSignature {
    public static void main(String[] args) {
        try {
            String inputFile = "C:\\Documents\\foldername\\digital.txt";

            KeyPairGenerator keyGen = KeyPairGenerator.getInstance("DSA", "SUN");
            SecureRandom random = SecureRandom.getInstance("SHA1PRNG", "SUN");
            keyGen.initialize(1024, random);
            KeyPair pair = keyGen.generateKeyPair();
            PrivateKey priv = pair.getPrivate();
            PublicKey pub = pair.getPublic();

            Signature dsa = Signature.getInstance("SHA1withDSA", "SUN");
            dsa.initSign(priv);

            try (FileInputStream fis = new FileInputStream(inputFile);
                 BufferedInputStream bufin = new BufferedInputStream(fis)) {
                byte[] buffer = new byte[1024];
                int len;
                while ((len = bufin.read(buffer)) != -1) {
                    dsa.update(buffer, 0, len);
                }
            }

            byte[] realSig = dsa.sign();

            try (FileOutputStream sigfos = new FileOutputStream("C:\\Documents\\foldername\\signature.txt")) {
                sigfos.write(realSig);
            }

            byte[] key = pub.getEncoded();
            try (FileOutputStream keyfos = new FileOutputStream("C:\\Documents\\foldername\\publickey.txt")) {
                keyfos.write(key);
            }

            System.out.println("Digital signature generated successfully!");
            System.out.println("Signature saved at: C:\\Documents\\foldername\\signature.txt");
            System.out.println("Public key saved at: C:\\Documents\\foldername\\publickey.txt");

        } catch (Exception e) {
            System.err.println("Caught exception: " + e);
            e.printStackTrace();
        }
    }
}