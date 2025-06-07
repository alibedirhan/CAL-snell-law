import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches

class SnellLawSimulator:
    def __init__(self):
        # Farklı malzemelerin kırılma indisleri
        self.materials = {
            'Hava': 1.00,
            'Su': 1.33,
            'Cam': 1.52,
            'Elmas': 2.42,
            'Akrilik': 1.49,
            'Silikon': 3.42
        }
        
        # Başlangıç parametreleri
        self.n1 = 1.00  # üst ortam
        self.n2 = 1.33  # alt ortam  
        self.theta1 = 30  # geliş açısı
        
        self.setup_plot()
    
    def setup_plot(self):
        """Ana pencereyi ve layout'u hazırla"""
        # Toolbar'ı gizle
        plt.rcParams['toolbar'] = 'None'
        
        # Ana figürü oluştur
        self.fig = plt.figure(figsize=(18, 10))
        self.fig.suptitle('Snell Kanunu Simulatoru', fontsize=20, fontweight='bold')
        
        # Pencere başlığını ayarla
        self.fig.canvas.manager.set_window_title('CAL')
        
        # Grid layout - 3x3 düzeni
        gs = self.fig.add_gridspec(3, 3, 
                                  height_ratios=[2, 1, 0.8], 
                                  width_ratios=[2, 1, 1],
                                  left=0.05, bottom=0.15, right=0.95, top=0.9,
                                  hspace=0.4, wspace=0.3)
        
        # Alt panelleri tanımla
        self.ax_main = self.fig.add_subplot(gs[0:2, 0])      # ana çizim
        self.ax_calc = self.fig.add_subplot(gs[0, 1:])       # hesaplamalar
        self.ax_result = self.fig.add_subplot(gs[1, 1:])     # sonuçlar
        
        self.setup_main_plot()
        self.setup_controls()
        self.update_simulation(None)
    
    def setup_main_plot(self):
        """Ana çizim alanının temel ayarları"""
        self.ax_main.set_xlim(-150, 150)
        self.ax_main.set_ylim(-150, 150)
        self.ax_main.set_aspect('equal')
        self.ax_main.set_title('Isik Isinlarinin Davranisi', fontsize=16, pad=20)
        self.ax_main.grid(True, alpha=0.3)
        self.ax_main.set_xlabel('X Ekseni', fontsize=12)
        self.ax_main.set_ylabel('Y Ekseni', fontsize=12)
    
    def setup_controls(self):
        """Slider ve buton kontrollerini ayarla"""
        # Slider konumları
        left_pos = 0.1
        width = 0.25
        height = 0.02
        
        # Açı slider'ı
        ax_theta = plt.axes([left_pos, 0.08, width, height])
        self.slider_theta1 = Slider(ax_theta, 'Gelis Acisi', 5, 85, 
                                   valinit=self.theta1, valfmt='%.0f°')
        
        # n1 slider'ı
        ax_n1 = plt.axes([left_pos, 0.05, width, height])
        self.slider_n1 = Slider(ax_n1, 'n1 (Ust ortam)', 1.0, 3.0, 
                               valinit=self.n1, valfmt='%.2f')
        
        # n2 slider'ı
        ax_n2 = plt.axes([left_pos, 0.02, width, height])
        self.slider_n2 = Slider(ax_n2, 'n2 (Alt ortam)', 1.0, 3.0, 
                               valinit=self.n2, valfmt='%.2f')
        
        # Hızlı seçim butonları
        btn_w = 0.08
        btn_h = 0.03
        btn_y = 0.11
        
        ax_btn1 = plt.axes([0.45, btn_y, btn_w, btn_h])
        ax_btn2 = plt.axes([0.54, btn_y, btn_w, btn_h])
        ax_btn3 = plt.axes([0.63, btn_y, btn_w, btn_h])
        ax_btn4 = plt.axes([0.72, btn_y, btn_w, btn_h])
        
        self.btn_air_water = Button(ax_btn1, 'Hava→Su')
        self.btn_water_air = Button(ax_btn2, 'Su→Hava')
        self.btn_glass_air = Button(ax_btn3, 'Cam→Hava')
        self.btn_reset = Button(ax_btn4, 'Sifirla')
        
        # Event bağlantıları
        self.slider_theta1.on_changed(self.update_simulation)
        self.slider_n1.on_changed(self.update_simulation)
        self.slider_n2.on_changed(self.update_simulation)
        
        self.btn_air_water.on_clicked(lambda x: self.set_materials(1.00, 1.33))
        self.btn_water_air.on_clicked(lambda x: self.set_materials(1.33, 1.00))
        self.btn_glass_air.on_clicked(lambda x: self.set_materials(1.52, 1.00))
        self.btn_reset.on_clicked(lambda x: self.reset_simulation())
    
    def reset_simulation(self):
        """Varsayılan değerlere dön"""
        self.slider_theta1.set_val(30)
        self.slider_n1.set_val(1.00)
        self.slider_n2.set_val(1.33)
    
    def set_materials(self, n1, n2):
        """Önceden tanımlı malzeme çiftlerini ayarla"""
        self.slider_n1.set_val(n1)
        self.slider_n2.set_val(n2)
    
    def calculate_snell(self, theta1_deg, n1, n2):
        """Snell yasası hesaplaması yap"""
        theta1_rad = np.radians(theta1_deg)
        
        # n1 * sin(θ1) = n2 * sin(θ2)
        sin_theta2 = (n1 * np.sin(theta1_rad)) / n2
        
        results = {
            'theta1': theta1_deg,
            'n1': n1,
            'n2': n2,
            'sin_theta2': sin_theta2,
            'total_internal_reflection': False,
            'theta2': None,
            'critical_angle': None
        }
        
        # Kritik açıyı hesapla (sadece n1 > n2 ise)
        if n1 > n2:
            results['critical_angle'] = np.degrees(np.arcsin(n2 / n1))
        
        # Tam iç yansıma var mı?
        if abs(sin_theta2) > 1:
            results['total_internal_reflection'] = True
        else:
            results['theta2'] = np.degrees(np.arcsin(sin_theta2))
        
        return results
    
    def draw_ray_diagram(self, results):
        """Işın diyagramını çiz"""
        self.ax_main.clear()
        self.ax_main.set_xlim(-150, 150)
        self.ax_main.set_ylim(-150, 150)
        self.ax_main.set_aspect('equal')
        self.ax_main.grid(True, alpha=0.3)
        self.ax_main.set_title('Isik Isinlarinin Davranisi', fontsize=16)
        self.ax_main.set_xlabel('X Ekseni', fontsize=12)
        self.ax_main.set_ylabel('Y Ekseni', fontsize=12)
        
        # Ortamları ayıran çizgi
        self.ax_main.axhline(y=0, color='black', linewidth=4, linestyle='-', alpha=0.8)
        
        # Ortam renklerini göster
        upper_rect = patches.Rectangle((-150, 0), 300, 150, 
                                     facecolor='lightblue', alpha=0.15)
        lower_rect = patches.Rectangle((-150, -150), 300, 150, 
                                     facecolor='lightcoral', alpha=0.15)
        self.ax_main.add_patch(upper_rect)
        self.ax_main.add_patch(lower_rect)
        
        # Ortam bilgilerini yaz
        self.ax_main.text(-130, 120, f'ORTAM 1\nn₁ = {results["n1"]:.2f}', 
                         fontsize=10, weight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", 
                                 facecolor="white", alpha=0.9, edgecolor='blue'))
        
        self.ax_main.text(-130, -120, f'ORTAM 2\nn₂ = {results["n2"]:.2f}', 
                         fontsize=10, weight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", 
                                 facecolor="white", alpha=0.9, edgecolor='red'))
        
        # Normal çizgisi
        self.ax_main.axvline(x=0, color='gray', linewidth=2, linestyle=':', alpha=0.7)
        self.ax_main.text(5, 130, 'Normal', fontsize=9, rotation=90, va='top')
        
        # Işınları çiz
        ray_length = 100
        theta1_rad = np.radians(results['theta1'])
        
        # Gelen ışın
        start_x = -ray_length * np.sin(theta1_rad)
        start_y = ray_length * np.cos(theta1_rad)
        
        self.ax_main.arrow(start_x, start_y, -start_x, -start_y, 
                          head_width=8, head_length=15, fc='red', ec='red', 
                          linewidth=4, alpha=0.8)
        
        # Gelen ışın açısını göster (soldan)
        self.draw_angle_arc(0, 0, 40, 90, 90+results['theta1'], 'red', f"θ₁={results['theta1']:.0f}°")
        
        if results['total_internal_reflection']:
            # Yansıyan ışın (simetrik olarak sol tarafa)
            end_x = -ray_length * np.sin(theta1_rad)
            end_y = ray_length * np.cos(theta1_rad)
            
            self.ax_main.arrow(0, 0, end_x, end_y, 
                              head_width=8, head_length=15, fc='green', ec='green', 
                              linewidth=4, alpha=0.8)
            
            # Yansıyan ışın açısını göster
            self.draw_angle_arc(0, 0, 50, 90, 90+results['theta1'], 'green', f"θ_yansıma={results['theta1']:.0f}°")
            
            # Uyarı mesajı
            self.ax_main.text(0, -80, 'TAM İÇ YANSIMA', 
                             ha='center', va='center', fontsize=11, weight='bold',
                             bbox=dict(boxstyle="round,pad=0.3", 
                                     facecolor="yellow", alpha=0.8))
        else:
            # Kırılan ışın
            theta2_rad = np.radians(results['theta2'])
            end_x = ray_length * np.sin(theta2_rad)
            end_y = -ray_length * np.cos(theta2_rad)
            
            self.ax_main.arrow(0, 0, end_x, end_y, 
                              head_width=8, head_length=15, fc='blue', ec='blue', 
                              linewidth=4, alpha=0.8)
            
            # Kırılan ışın açısını göster
            self.draw_angle_arc(0, 0, 60, -90, -90+results['theta2'], 'blue', f"θ₂={results['theta2']:.0f}°")
        
        # Legend ekle
        legend_items = [plt.Line2D([0], [0], color='red', lw=4, label='Gelen Işın')]
        
        if results['total_internal_reflection']:
            legend_items.append(plt.Line2D([0], [0], color='green', lw=4, label='Yansıyan Işın'))
        else:
            legend_items.append(plt.Line2D([0], [0], color='blue', lw=4, label='Kırılan Işın'))
            
        self.ax_main.legend(handles=legend_items, loc='upper right', fontsize=10)
    
    def draw_angle_arc(self, x, y, radius, start_angle, end_angle, color, label):
        """Açı yayını çiz"""
        angles = np.linspace(np.radians(start_angle), np.radians(end_angle), 50)
        arc_x = x + radius * np.cos(angles)
        arc_y = y + radius * np.sin(angles)
        self.ax_main.plot(arc_x, arc_y, color=color, linewidth=3)
        
        # Açı etiketini yerleştir
        mid_angle = np.radians((start_angle + end_angle) / 2)
        label_x = x + (radius + 15) * np.cos(mid_angle)
        label_y = y + (radius + 15) * np.sin(mid_angle)
        self.ax_main.text(label_x, label_y, label, fontsize=9, weight='bold',
                         ha='center', va='center', color=color)
    
    def display_calculations(self, results):
        """Hesaplama detaylarını göster"""
        self.ax_calc.clear()
        self.ax_calc.set_xlim(0, 1)
        self.ax_calc.set_ylim(0, 1)
        self.ax_calc.axis('off')
        self.ax_calc.set_title('Hesaplama Detaylari', fontsize=14, weight='bold')
        
        # Formül
        formula_text = "SNELL KANUNU\nn₁ × sin(θ₁) = n₂ × sin(θ₂)"
        self.ax_calc.text(0.5, 0.92, formula_text, ha='center', va='center', 
                         fontsize=10, weight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8))
        
        # Girdi değerleri
        input_text = f"VERİLEN DEĞERLER\nn₁={results['n1']:.2f}  n₂={results['n2']:.2f}  θ₁={results['theta1']:.0f}°"
        self.ax_calc.text(0.5, 0.68, input_text, ha='center', va='center', 
                         fontsize=9, weight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.8))
        
        # Hesaplama adımları
        steps_text = f"""HESAPLAMA ADIMLARI
sin(θ₂) = (n₁/n₂) × sin(θ₁)
sin(θ₂) = ({results['n1']:.2f}/{results['n2']:.2f}) × sin({results['theta1']:.0f}°)
sin(θ₂) = {results['sin_theta2']:.4f}"""
        
        self.ax_calc.text(0.5, 0.45, steps_text, ha='center', va='center', 
                         fontsize=9, family='monospace',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8))
    
    def display_results(self, results):
        """Sonuç panelini göster"""
        self.ax_result.clear()
        self.ax_result.set_xlim(0, 1)
        self.ax_result.set_ylim(0, 1)
        self.ax_result.axis('off')
        self.ax_result.set_title('Sonuclar', fontsize=14, weight='bold')
        
        if results['total_internal_reflection']:
            # Tam iç yansıma durumu
            main_result = "TAM İÇ YANSIMA"
            self.ax_result.text(0.5, 0.90, main_result, ha='center', va='center', 
                               fontsize=10, weight='bold',
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral", alpha=0.8))
            
            # Kritik açı
            critical_text = f"KRİTİK AÇI\n{results['critical_angle']:.1f}°"
            self.ax_result.text(0.5, 0.70, critical_text, ha='center', va='center', 
                               fontsize=9, weight='bold',
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="orange", alpha=0.8))
            
            # Koşul
            condition_text = f"θ₁ = {results['theta1']:.0f}° > {results['critical_angle']:.1f}°"
            self.ax_result.text(0.5, 0.52, condition_text, ha='center', va='center', fontsize=9)
            
        else:
            # Normal kırılma
            main_result = f"KIRILMA AÇISI\nθ₂ = {results['theta2']:.1f}°"
            self.ax_result.text(0.5, 0.90, main_result, ha='center', va='center', 
                               fontsize=10, weight='bold',
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.8))
            
            # Durum
            status_text = "Normal kırılma gerçekleşti"
            self.ax_result.text(0.5, 0.70, status_text, ha='center', va='center', 
                               fontsize=9, weight='bold',
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8))
            
            # Kritik açı bilgisi (sadece n1 > n2 ise)
            if results['critical_angle'] is not None:
                critical_info = f"Kritik açı: {results['critical_angle']:.1f}°"
                self.ax_result.text(0.5, 0.52, critical_info, ha='center', va='center', fontsize=9)
        
        # Fizik kuralları
        physics_rules = """FİZİK KURALLARI
• Yoğun → Seyrek: Işın normalden uzaklaşır
• Seyrek → Yoğun: Işın normale yaklaşır  
• Tam iç yansıma: sadece n₁ > n₂ ise mümkün
• Kritik açı: θc = arcsin(n₂/n₁)"""
        
        self.ax_result.text(0.5, 0.20, physics_rules, ha='center', va='center', 
                           fontsize=8,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.7))
    
    def update_simulation(self, val):
        """Tüm grafikleri güncelle"""
        self.theta1 = self.slider_theta1.val
        self.n1 = self.slider_n1.val
        self.n2 = self.slider_n2.val
        
        # Hesaplamaları gerçekleştir
        results = self.calculate_snell(self.theta1, self.n1, self.n2)
        
        # Grafikleri yenile
        self.draw_ray_diagram(results)
        self.display_calculations(results)
        self.display_results(results)
        
        # Ekranı güncelle
        self.fig.canvas.draw()
    
    def show(self):
        """Uygulamayı göster"""
        plt.show()

# Program başlangıcı
if __name__ == "__main__":
    try:
        print("Snell Kanunu Simulatoru baslatiliyor...")
        sim = SnellLawSimulator()
        sim.show()
    except KeyboardInterrupt:
        print("\nProgram sonlandirildi.")
    except Exception as e:
        print(f"Hata olustu: {e}")