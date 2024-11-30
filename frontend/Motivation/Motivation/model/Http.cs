using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net.Http.Json;
using System.Collections.ObjectModel;
namespace Motivation.model
{
    class Http
    {
        //хранит строку с ссылкой к api
        const string api = "http://10.199.180.150:8000";
        //используется для отправки и приема пакетов
        HttpClient http = new HttpClient();
        //метод отправки логина и получения id сотрудника
        async Task<Sotrudnik> HttpLogin(Login login)
        {
            // результат которая будет использована в возврате метода
            Sotrudnik result;
            //создаем пакет json для отправки
            JsonContent content = JsonContent.Create(login);
            //пост запрос на сервер
            var response = await http.PostAsync(api + "/password", content);
            //обработка кодов для отлова ошибок
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception($"Ошибка Клиента: {response.Content.ReadAsStringAsync()}");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                //десериализация результата
                result = await response.Content.ReadFromJsonAsync<Sotrudnik>();
                return result;
            }
            else
            {
                //в случае других кодов выдать исключение
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode}{response.Content.ReadAsStringAsync()}");
            }
        }
        //метод получения списка сделок по id сотрудника
        async Task<ObservableCollection<Deal>> HttpDeals(string id)
        {
            //Коллекция сделок сделанная специально для последующего отслеживания событий
            ObservableCollection<Deal> deal;
            //создание пакета
            JsonContent content = JsonContent.Create(id);
            //отправка пакета
            var response = await http.PostAsync(api + "/deals", content);
            //обработка кодов для отлова ошибок
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception($"Ошибка Сделки не найдены: {response.Content.ReadAsStringAsync()}") ;
            }
            else if (response.StatusCode.ToString() == "200")
            {
                //десериализация ответа
                deal =await response.Content.ReadFromJsonAsync<ObservableCollection<Deal>>();
                return deal;
            }
            else
            {
                //в случае других кодов выдать исключение
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode} {response.Content.ReadAsStringAsync()}");
            }
        }
        //метод возврата списка рейтинга сотрудников
        async Task<ObservableCollection<Rating>> HttpRating(string id)
        {
            ObservableCollection<Rating> rating;
            var response = await http.PostAsync(api + "/rating", null);
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception("Рейтинг не найден");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                rating = await response.Content.ReadFromJsonAsync<ObservableCollection<Rating>>();
                return rating;
            }
            else
            {
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode} {response.Content.ReadAsStringAsync()}");
            }
        }
        //метод получения зарплаты по конкретному месяцу
        async Task<OutputSalary> HttpMonthSalary(string id,DateTime month)
        {
            //пакет для отправки
            InputSalary sal = new InputSalary(id, month);
            //сериализуем его в json
            JsonContent content = JsonContent.Create(sal);
            //результат
            OutputSalary output;
            //отправка пакета
            var response = await http.PostAsync(api + "/salary/month", content);
            if (response.StatusCode.ToString() == "400")
            {
                //ошибки с сервера
                throw new Exception($"Зарплата не найдена: {response.Content.ReadAsStringAsync()}");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                //десериализация ответа
                output = await response.Content.ReadFromJsonAsync<OutputSalary>();
                return output;
            }
            else
            {
                //отлов ошибок
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode} {response.Content.ReadAsStringAsync()}");
            }
        }
}
}
