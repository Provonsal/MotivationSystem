using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
   public class InputSalary
    {
        string id;
        DateTime month;
        public InputSalary(string id, DateTime month)
        {
            this.id = id;
            this.month = month;
        }
    }
}
