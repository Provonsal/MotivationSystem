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
        string id;
        //поле фамилии
        string firstname;
        //поле отчество
        string surname;
        //поле имя
        string lastname;
        //поле харплата
        UInt32 salary;
        //поле премия
        UInt16 bonus;
    }
}
