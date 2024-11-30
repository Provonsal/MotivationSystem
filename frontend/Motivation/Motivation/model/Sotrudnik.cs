using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //хранит информацию о текущем сотруднике
    public class Sotrudnik
    {
        // id сотрудника
        public string id;
        // фамилия сотрудника
        public string firstname;
        //имя сотрудника
        public string lastname;
        //отчество сотрудника
        public string surname;
        public Sotrudnik(string id, string name, string lastname, string surname)
        {
            this.id = id;
            this.firstname = name;
            this.lastname = lastname;
            this.surname = surname;
        }
    }
}
