using System;
using System.Drawing;
using System.Windows.Forms;
using ml_qubit;

namespace ml_qubit
{
    class DrawWindow : Form
    {
        public DrawWindow() //this constructor draws the form
        {
            InitializeComponent();
        }


        private void InitializeComponent()
        {
            this.SuspendLayout();
            // DrawWindow
            this.ClientSize = new System.Drawing.Size(800, 800);
            this.Location = new System.Drawing.Point(10, 10);
            this.Name = "DrawWindow";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.DrawWindow_Paint);
            this.ResumeLayout(false);
        }

        private void DrawWindow_Paint(object sender, PaintEventArgs e)
        {
            Graphics Grf = e.Graphics;
            MiraPlot(Grf);
            SinusPlot(Grf);
        }

        private void SinusPlot(Graphics Grf)
        {
            Plot MyPlot = new Plot();
            double x = 0.0;
            double y = 0.0;
            MyPlot.ClientArea = this.ClientSize;
            MyPlot.SetPlotPort(-10, 10, -5, 5);
            for (x = -7.0; x < 10.0; x += 0.025)
            {
                y = Math.Sin(x);
                MyPlot.PlotPixel(x, y, Color.BlueViolet, Grf);
            }
        }

        private void MiraPlot(Graphics Grf)
        {
            Plot MyPlot = new Plot();
            double a = -0.46;
            double b = 0.99;
            double c = 2.0 - 2.0 * a;
            double x = 12.0;    //start value
            double y = 0.0;     //start value
            double z;
            double w = a * x + c * x * x / (1 + x * x);

            MyPlot.ClientArea = this.ClientSize;
            MyPlot.SetPlotPort(-20, 20, -20, 20);
            for (int n = 0; n < 20000; n++)
            {
                MyPlot.PlotPixel(x, y, Color.BlueViolet, Grf);
                z = x;
                x = b * y + w;
                w = a * x + c * x * x / (1 + x * x);
                y = w - z;
            }
        }
    }


    class Plot
    {
        //class to plot x and y values on a form
        //
        //because on the form coordinates start at the upper left corner with 0,0
        //with the y coordinate going down, a little transformation is done here
        //so that x,y coordinates act as normal carthesian coordinates, with 0,0
        //in the center of the form

        struct PlotPort
        {
            public int minX;
            public int maxX;
            public int minY;
            public int maxY;
        };

        private PlotPort _PlotW;    //"window" of carthesian coordinates
        private Size _ClientArea;   //keeps the pixels info
        private double _Xspan;
        private double _Yspan;

        public Plot() { }

        public Plot(Size Plotarea)
        {
            _ClientArea = Plotarea;
        }

        public Size ClientArea { set { _ClientArea = value; } }

        public void SetPlotPort(int minx, int maxx, int miny, int maxy)
        {
            //set the bounderies of the form(screen) to real coordinates.
            _PlotW.minX = minx;
            _PlotW.maxX = maxx;
            _PlotW.minY = miny;
            _PlotW.maxY = maxy;
            _Xspan = _PlotW.maxX - _PlotW.minX;
            _Yspan = _PlotW.maxY - _PlotW.minY;
        }

        public void PlotPixel(double X, double Y, Color C, Graphics G)
        {
            //workhorse of this class
            Bitmap bm = new Bitmap(1, 1);
            bm.SetPixel(0, 0, C);
            G.DrawImageUnscaled(bm, TX(X), TY(Y));
        }

        private int TX(double X) //transform real coordinates to pixels for the X-axis
        {
            double w;
            w = _ClientArea.Width / _Xspan * X + _ClientArea.Width / 2;
            return Convert.ToInt32(w);
        }

        private int TY(double Y) //transform real coordinates to pixels for the Y-axis
        {
            double w;
            w = _ClientArea.Height / _Yspan * Y + _ClientArea.Height / 2;
            return Convert.ToInt32(w);
        }
    }
}