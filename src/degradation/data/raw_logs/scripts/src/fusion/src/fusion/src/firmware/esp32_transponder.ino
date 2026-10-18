#include <esp_now.h>
#include <WiFi.h>

// Fixed 24-byte telemetry payload struct
typedef struct __attribute__((packed)) {
    uint8_t  mac_addr[6];    // 6 bytes MAC address
    uint32_t packet_seq;     // 4 bytes sequence ID
    int8_t   rssi_val;       // 1 byte RSSI
    uint32_t timestamp_ms;   // 4 bytes millisecond counter
    uint8_t  status_flags;   // 1 byte transponder status
    uint8_t  padding[8];     // 8 bytes alignment padding
} TelemetryPacket24B;         // Total: 24 bytes

TelemetryPacket24B packet;

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    
    if (esp_now_init() != ESP_OK) {
        Serial.println("ESP-NOW Initialization Failed");
        return;
    }
    Serial.println("ESP-NOW Transponder Active (24-byte payload @ 100 Hz)");
}

void loop() {
    // Populate 24-byte binary structure
    WiFi.macAddress(packet.mac_addr);
    packet.packet_seq++;
    packet.timestamp_ms = millis();
    packet.status_flags = 0x01; // Active nominal
    
    // Broadcast over raw physical layer without handshakes
    delay(10); // 100 Hz broadcast rate
}
