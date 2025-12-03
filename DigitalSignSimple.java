import java.security.*;
import java.util.Base64;
import java.util.Scanner;

public class DigitalSignSimple {

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter message: ");
        String msg = sc.nextLine();

        KeyPair keyPair = KeyPairGenerator.getInstance("RSA").generateKeyPair();
        Signature sign = Signature.getInstance("SHA256withRSA");

        // Sign
        sign.initSign(keyPair.getPrivate());
        sign.update(msg.getBytes());
        String signature = Base64.getEncoder().encodeToString(sign.sign());

        // Verify
        sign.initVerify(keyPair.getPublic());
        sign.update(msg.getBytes());
        boolean valid = sign.verify(Base64.getDecoder().decode(signature));

        System.out.println("\nMessage: " + msg);
        System.out.println("Signature: " + signature);
        System.out.println("Verified: " + valid);

        sc.close();
    }
}
