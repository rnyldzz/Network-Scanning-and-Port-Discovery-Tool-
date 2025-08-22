### **Ağ Taraması ve Port Tespiti Aracı (Python)**

Bu depo, Python programlama dilini kullanarak geliştirilmiş basit ama işlevsel bir ağ tarama ve port tespit aracını barındırır. Projenin temel amacı, bir hedef IP adresi veya alan adı üzerindeki açık TCP portlarını belirlemek ve bu portlar hakkında temel bilgiler sunmaktır. Bu araç, siber güvenlik alanına ilgi duyanlar, ağ protokolleri hakkında bilgi edinmek isteyen öğrenciler veya basit bir ağ keşif aracı arayanlar için ideal bir başlangıç noktasıdır.

**Proje Amacı ve Önemi**

Modern ağ altyapıları, sunucular ve hizmetler, çeşitli portlar üzerinden iletişim kurar. Açık portlar, bir sunucunun hangi hizmetleri (örneğin, bir web sunucusu, bir SSH sunucusu veya bir veritabanı) dış dünyaya sunduğunu gösterir. Bu araç, bir sistem yöneticisinin veya güvenlik analistinin, kendi ağındaki cihazların beklenmedik portları açık bırakıp bırakmadığını kontrol etmesine olanak tanır. Kötü amaçlı yazılımlar genellikle gizli portları açarak arka kapılar oluşturur. Bu araç, bu tür potansiyel güvenlik zafiyetlerinin hızlı bir şekilde tespit edilmesine yardımcı olabilir.

**Temel Özellikler**

* **Esnek Hedef Belirleme:** Kullanıcı, tarama için bir IP adresi (örneğin, `192.168.1.1`) veya bir alan adı (örneğin, `example.com`) girebilir. Program, alan adını otomatik olarak IP adresine dönüştürür.
* **Özelleştirilebilir Port Aralığı:** Varsayılan olarak 1-1024 arasındaki bilinen portları tarar, ancak bu aralık kolayca değiştirilebilir ve genişletilebilir.
* **Çoklu Bağlantı Kontrolü:** `socket` modülünü kullanarak her bir port için ayrı bir bağlantı denemesi yapar.
* **Etkin Zaman Aşımı Yönetimi:** Bağlantı denemelerinde yaşanan gecikmeleri önlemek için bir zaman aşımı (timeout) mekanizması içerir, böylece tarama işlemi donmaz ve verimli bir şekilde tamamlanır.
* **Anlaşılır Raporlama:** Açık bulunan portları ve varsa ilişkili hizmetleri (örneğin, `Port 80 açık [HTTP]`) anlaşılır bir formatta raporlar.
* **Hata Yönetimi:** Geçersiz bir hedef girişi veya ağ bağlantı sorunları gibi durumlar için kullanıcı dostu hata mesajları sunar.

**Teknik Detaylar**

Bu proje, Python'ın standart kütüphanelerinden olan `socket` modülünün gücünden yararlanır. TCP/IP protokolü ve soket programlamanın temel ilkeleri üzerine inşa edilmiştir. Kod, temiz ve anlaşılır bir yapıya sahiptir, bu sayede hem yeni başlayanlar hem de deneyimli geliştiriciler tarafından rahatlıkla okunabilir ve üzerinde değişiklik yapılabilir.

Bu aracı kullanarak, ağ keşifleri yapabilir, potansiyel güvenlik açıklarını belirleyebilir ve temel ağ iletişimi prensiplerini uygulamalı olarak öğrenebilirsiniz. Projenin daha fazla geliştirilmesi ve yeni özelliklerin eklenmesi için katkılarınız her zaman bekleriz.

-
