using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //класс рейтинг хранящая информацию о сотруднике и рейтинге
    public class Rating
    {
        //поле id
        public string id;
        //поле фамилии
        public string firstname;
        //поле отчество
        public string surname;
        //поле имя
        public string lastname;
        //поле харплата
        public UInt32 salary;
        //поле премия
        public UInt16 bonus;
    }
}
