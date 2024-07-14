package dbmsproj;

import javax.swing.*;
import java.awt.*;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

public class box {
    public static void createAndShowGUI() {
        JFrame f = new JFrame("Customer Page");//creating instance of JFrame

        Color coral = new Color(89, 167, 245, 247);
        f.getContentPane().setBackground(coral);


        JButton button2 = new JButton("Track");
        button2.setBounds(150, 240, 100, 40);

        JTextField textField = new JTextField();
        textField.setBounds(130, 140, 180, 30); // x axis, y axis, width, height
        addPlaceholderText(textField, "Enter your Order No.");

        JLabel orderNoLabel = new JLabel("Order No.");
        orderNoLabel.setBounds(130, 120, 80, 30);
        orderNoLabel.setForeground(Color.WHITE);

        JLabel phoneNoLabel = new JLabel("Phone No.");
        phoneNoLabel.setBounds(130, 170, 80, 30);
        phoneNoLabel.setForeground(Color.WHITE);

        JTextField textField2 = new JTextField();
        textField2.setBounds(130, 190, 180, 30); // x axis, y axis, width, height
        addPlaceholderText(textField2, "Enter your Phno.");

        f.add(textField);
        f.add(orderNoLabel);
        f.add(phoneNoLabel);
        f.add(button2);
        f.add(textField2);


        f.setSize(400, 500);//400 width and 500 height
        f.setLayout(null);//using no layout managers
        f.setVisible(true);//making the frame visible


    }
    private static void addPlaceholderText(JTextField textField, String placeholder) {
        // Add a FocusListener to handle placeholder text
        textField.setForeground(Color.GRAY);
        textField.setText(placeholder);

        textField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (textField.getText().equals(placeholder)) {
                    textField.setText("");
                    textField.setForeground(Color.BLACK);
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (textField.getText().isEmpty()) {
                    textField.setForeground(Color.GRAY);
                    textField.setText(placeholder);
                }
            }
        });
    }

}
