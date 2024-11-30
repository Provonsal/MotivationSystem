using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Motivation.model
{
    //хранит информацию о текущем сотруднике
    class Sotrudnik
    {
        // id сотрудника
        string id;
        // фамилия сотрудника
        string firstname;
        //имя сотрудника
        string lastname;
        //отчество сотрудника
        string surname;
        public Sotrudnik(string id, string name, string lastname, string surname)
        {
            this.id = id;
            this.firstname = name;
            this.lastname = lastname;
            this.surname = surname;
        }
    }
}
