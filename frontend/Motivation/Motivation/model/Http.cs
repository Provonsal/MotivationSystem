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
        const string api = "http://10.199.180.150:8000";
        HttpClient http = new HttpClient();
        async Task<string> HttpLogin(Login login)
        {
            string result;
            JsonContent content = JsonContent.Create(login);
            var response = await http.PostAsync(api + "/password", content);
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception("Ошибка Клиента");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                result = await response.Content.ReadAsStringAsync();
                result = result.Substring(0, result.Length - result.LastIndexOf(':'));
                result = result.Substring(result.Length);
                return result;
            }
            else
            {
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode}");
            }
        }
        async Task<ObservableCollection<Deal>> HttpDeals(string id)
        {
            ObservableCollection<Deal> deal;
            JsonContent content = JsonContent.Create(id);
            var response = await http.PostAsync(api + "/deals", content);
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception("Ошибка Сделки не найдены");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                deal =await response.Content.ReadFromJsonAsync<ObservableCollection<Deal>>();
                return deal;
            }
            else
            {
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode}");
            }
        }
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
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode}");
            }
        }
        async Task<OutputSalary> HttpMonthSalary(string id,DateTime month)
        {
            InputSalary sal = new InputSalary(id, month);
            JsonContent content = JsonContent.Create(sal);
            OutputSalary output;
            var response = await http.PostAsync(api + "/salary/month", content);
            if (response.StatusCode.ToString() == "400")
            {
                throw new Exception("Зарплата не найдена");
            }
            else if (response.StatusCode.ToString() == "200")
            {
                output = await response.Content.ReadFromJsonAsync<OutputSalary>();
                return output;
            }
            else
            {
                throw new Exception($"Ошибка сервер вернул статус код: {response.StatusCode}");
            }
        }
}
}
