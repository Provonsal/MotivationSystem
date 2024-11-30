﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using Motivation.model;
namespace Motivation
{
    public class MainVieModel : INotifyPropertyChanged
    {
        Sotrudnik id;
        public MainVieModel(Sotrudnik idsotr)
        {
           id = idsotr;
           
           
        }

        private string firsname;
        public string Firstname
        {
            get
            {
                return firsname;
            }
            set
            {
                firsname = value;
                OnPropertyChanged(nameof(firsname));
            }
        }
        private string lastname;
        public string Lastname
        {
            get
            {
                return lastname;
            }
            set
            {
                lastname = value;
                OnPropertyChanged(nameof(lastname));
            }
        }
        private string surname;
        public string Surname
        {
            get
            {
                return surname;
            }
            set
            {
                surname = value;
                OnPropertyChanged(nameof(surname));
            }
        }
        string year = DateTime.Now.Year.ToString();
        static string [] month  = { "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" };;

        int selectdmonth;
        
        int SelectedMonth
        {
            get
            {
                return selectdmonth;
            }
            set
            {
                selectdmonth = value;
                OnPropertyChanged(nameof(selectdmonth));
            }
        }


        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }
    }
}
