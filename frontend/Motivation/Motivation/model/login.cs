using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;
namespace Motivation
{
    //используется для промежуточного сохранения логина и пароля для последующей отправки
    class Login
    {
        string login;
        string password;
        //конструктор для создание записи логина и хеширования пароля
       public Login(string log, string pass)
        {
            login = log;
            SHA256 sha = SHA256.Create();
            password = System.Text.Encoding.Default.GetString(sha.ComputeHash(Encoding.UTF8.GetBytes(pass)));
            //происходит хеширование пароля и преобразование его в строку для последующей отправки
        }
    }
}
