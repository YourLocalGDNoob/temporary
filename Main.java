import java.io.FileWriter;
import java.io.IOException;
class Main {
    public static void main(String[] args) throws IOException {
        FileWriter file = new FileWriter("equations.txt");
        for(int n0 = -25; n0 <= 25; n0++) {
            for(int n1 = -25; n1 <= 25; n1++) {
                for(int n2 = -25; n2 <= 25; n2++) {
                    for(int n3 = -25; n3 <= 25; n3++) {
                        for(int o0 = 1; o0 <= 4; o0++) {
                            for(int o1 = 1; o1 <= 4; o1++) {
                                for(int o2 = 1; o2 <= 4; o2++) {
                                    String O0 = "";
                                    String O1 = "";
                                    String O2 = "";

                                    if(o0 == 1) {
                                        O0 = " + ";
                                    }
                                    if(o0 == 2) {
                                        O0 = " - ";
                                    }
                                    if(o0 == 3) {
                                        O0 = " * ";
                                    }
                                    if(o0 == 4) {
                                        O0 = " / ";
                                    }

                                    if(o1 == 1) {
                                        O1 = " + ";
                                    }
                                    if(o1 == 2) {
                                        O1 = " - ";
                                    }
                                    if(o1 == 3) {
                                        O1 = " * ";
                                    }
                                    if(o1 == 4) {
                                        O1 = " / ";
                                    }

                                    if(o2 == 1) {
                                        O2 = " + ";
                                    }
                                    if(o2 == 2) {
                                        O2 = " - ";
                                    }
                                    if(o2 == 3) {
                                        O2 = " * ";
                                    }
                                    if(o2 == 4) {
                                        O2 = " / ";
                                    }

                                    if((n1 == 0 && O0 == " / ") || (n2 == 0 && O1 == " / ") || (n3 == 0 && O2 == " / ")) {
                                        file.write(n0+O0+n1+O1+n2+O2+n3+" = undefined\n");
                                        continue;
                                    }

                                    double result = n0;
                                    if(O0 == " + ") {
                                        result += n2;
                                    }
                                    if(O0 == " - ") {
                                        result -= n2;
                                    }
                                    if(O0 == " * ") {
                                        result *= n2;
                                    }
                                    if(O0 == " / ") {
                                        result /= n2;
                                    }

                                    if(O1 == " + ") {
                                        result += n3;
                                    }
                                    if(O1 == " - ") {
                                        result -= n3;
                                    }
                                    if(O1 == " * ") {
                                        result *= n3;
                                    }
                                    if(O1 == " / ") {
                                        result /= n3;
                                    }

                                    if(O2 == " + ") {
                                        result += n3;
                                    }
                                    if(O2 == " - ") {
                                        result -= n3;
                                    }
                                    if(O2 == " * ") {
                                        result *= n3;
                                    }
                                    if(O2 == " / ") {
                                        result /= n3;
                                    }
                                    file.write(n0+O0+n1+O1+n2+O2+n3+" = "+result+"\n");
                                }
                            }
                        }
                    }
                }
            }
        }
        file.close();
    }
}