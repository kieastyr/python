import javax.swing.JLabel;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class abc83c extends JFrame implements ActionListener{
	
	static JTextField xf,yf;
	static JButton b;
	static JLabel a;
	static long x,y;
	
	abc83c(){
		this.setLayout(null);
		
		xf=new JTextField();
		yf=new JTextField();
		b=new JButton("calculate");
		a=new JLabel();
		
		xf.setBounds(100,50,200,50);
		yf.setBounds(100,100,200,50);
		b.setBounds(100,200,200,50);
		a.setBounds(100,300,200,50);
		
		this.add(xf);
		this.add(yf);
		this.add(b);
		this.add(a);
		
		b.addActionListener(this);
	}
	
	public void calculate(){
		int count=0;
		while(x<=y){
			x*=2;
			count++;
		}
		
		a.setText(""+count);
	}
	
	public static void main(String[] args){
		abc83c a=new abc83c();
		a.setSize(400,400);
		a.setVisible(true);
		a.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	public void actionPerformed(ActionEvent e){
		x=Long.parseLong(xf.getText());
		y=Long.parseLong(yf.getText());
		calculate();
	}
}
