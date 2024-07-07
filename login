package dbmsproj;

import javax.swing.*;
import java.awt.*;

public class login {
    public static void main(String[] args) {
        JFrame f=new JFrame();

        Color coral = new Color(170,127,100);
        f.getContentPane().setBackground(coral);

        JButton button1 = new JButton("Login as Company");
        button1.setBounds(110, 160, 200, 40);

        JButton button2 = new JButton("Login as Customer");
        button2.setBounds(110, 200, 200, 40);

         button2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                box.createAndShowGUI();
            }
        });

        f.add(button1);
        f.add(button2);

        f.setSize(400,500);//400 width and 500 height
        f.setLayout(null);//using no layout managers
        f.setVisible(true);


    }
}
