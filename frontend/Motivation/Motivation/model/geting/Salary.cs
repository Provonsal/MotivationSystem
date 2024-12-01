using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //необходим для информации о зарплате по конкретному месяцу
    public class OutputSalary
    {
        //месяц зарплаты
        public DateTime month;
        //зарплата
        public UInt32 salary;
        //процент премии который сотрудник получил
        public UInt16 bonus;
        //конструктор с параметрами для заполнения всех полей
        public OutputSalary(DateTime mon, UInt32 sal, UInt16 bon)
        {
            month = mon;
            salary = sal;
            bonus = bon;
        }
    }
}
