﻿using Motivation.model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Motivation
{
    /// <summary>
    /// Логика взаимодействия для PageSotrudnik.xaml
    /// </summary>
    public partial class PageSotrudnik : UserControl
    {
        MainViewModel vm;
        public PageSotrudnik(MainViewModel vm)
        {
            InitializeComponent();
            this.vm = vm;
            DataContext = vm;
        }
    }
}
