using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //класс для информации о сделке
    class Deal
    {
        string id_deal;
        UInt32 sum;
        uint percent;
        DateTime date_deal_start;
        DateTime date_deal_end;
        //конструктор для заполнения базовых полей
        public Deal(string id, UInt32 sum, uint percent, DateTime start, DateTime end)
        {
            id_deal = id;
            this.sum = sum;
            this.percent = percent;
            date_deal_end = end;
            date_deal_start = start;
        }
    }
}
