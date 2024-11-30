using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //Класс используемый для отправки на сервере информации о месяце и id сотрудника
   public class InputSalary
    {
        //id сотрудника
        string id;
        //месяц снятия показания
        DateTime month;
        //Конструктор с параметрами id и месяц
        public InputSalary(string id, DateTime month)
        {
            this.id = id;
            this.month = month;
        }
    }
}
