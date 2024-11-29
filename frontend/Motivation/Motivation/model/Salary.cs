using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //необходим для информации о зарплате по конкретному месяцу
    class Salary
    {
        public DateTime month;
        public UInt32 salary;
        public UInt16 bonus;
        //конструктор с параметрами для заполнения всех полей
        public Salary(DateTime mon, UInt32 sal, UInt16 bon)
        {
            month = mon;
            salary = sal;
            bonus = bon;
        }
    }
}
