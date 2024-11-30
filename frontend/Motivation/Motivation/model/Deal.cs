using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //класс для информации о сделке
   public  class Deal
    {
        //id сделки
        string id_deal;
        //сумма сделки
        UInt32 sum;
        //процент от сделки
        uint percent;
        //дата начала сделки
        DateTime date_deal_start;
        //дата заключения сделки
        DateTime date_deal_end;
        //название продуаного объекта
        string selled;
        //конструктор для заполнения базовых полей
        public Deal(string id, UInt32 sum, uint percent, DateTime start, DateTime end,string sel)
        {
            id_deal = id;
            this.sum = sum;
            this.percent = percent;
            date_deal_end = end;
            date_deal_start = start;
            selled = sel;
        }
    }
}
