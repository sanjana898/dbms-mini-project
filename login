package dbmsproj;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class login {
    public static void main(String[] args) {
        JFrame f=new JFrame("Login page");

        Color coral = new Color(89, 167, 245, 247);
        f.getContentPane().setBackground(coral);

        BackgroundPanel backgroundPanel = new BackgroundPanel("/Users/sanjanajoshi/Documents/Engg/4th sem/DBMS/background.png", 0.5f);
        backgroundPanel.setLayout(null);


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

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                company.createAndShowGUI();
            }
        });


        backgroundPanel.add(button1);
        backgroundPanel.add(button2);

        f.setContentPane(backgroundPanel); // Set the custom panel as the content pane
        f.setVisible(true);

        //f.add(button1);
        //f.add(button2);


        f.setSize(400,500);//400 width and 500 height
        f.setLayout(null);//using no layout managers
        //f.setVisible(true);


    }
}
