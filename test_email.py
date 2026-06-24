import os
import urllib.request
import urllib.parse
import json

api_key     = os.environ.get("RESEND_API_KEY")
from_email  = os.environ.get("RESEND_FROM_EMAIL", "noreply@opertrack.com")
to_email    = "jesusgrullon20@gmail.com"

# ══════════════════════════════════════════════
#  TEMPLATE 1 — VERIFICACIÓN DE CUENTA
# ══════════════════════════════════════════════
template_verificacion = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/></head>
<body style="margin:0;padding:0;background:#F0F4F8;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#F0F4F8;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
        
        <!-- HEADER -->
        <tr>
          <td style="background:linear-gradient(135deg,#042C53 0%,#185FA5 100%);padding:36px 40px;text-align:center;">
            <table cellpadding="0" cellspacing="0" style="margin:0 auto;">
              <tr>
                <td style="padding-right:12px;vertical-align:middle;">
                  <!-- Logo SVG inline -->
                  <svg width="48" height="48" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="100" cy="100" r="88" fill="none" stroke="#378ADD" stroke-width="12"/>
                    <line x1="64" y1="132" x2="136" y2="132" stroke="#B5D4F4" stroke-width="4" stroke-linecap="round"/>
                    <rect x="64"  y="114" width="14" height="18" rx="3" fill="#B5D4F4"/>
                    <rect x="82"  y="100" width="14" height="32" rx="3" fill="#B5D4F4"/>
                    <rect x="100" y="82"  width="14" height="50" rx="3" fill="#E6F1FB"/>
                    <rect x="118" y="68"  width="14" height="64" rx="3" fill="#E6F1FB"/>
                    <line x1="70"  y1="128" x2="132" y2="64" stroke="white" stroke-width="5" stroke-linecap="round"/>
                    <polyline points="118,58 132,64 126,78" fill="none" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </td>
                <td style="vertical-align:middle;">
                  <span style="font-size:28px;font-weight:800;color:#ffffff;letter-spacing:-0.5px;">Oper</span>
                  <span style="font-size:28px;font-weight:300;color:#85B7EB;letter-spacing:-0.5px;">track</span>
                </td>
              </tr>
            </table>
            <p style="margin:12px 0 0;font-size:12px;color:rgba(255,255,255,0.5);letter-spacing:2px;">GESTIÓN DE EQUIPOS TÉCNICOS</p>
          </td>
        </tr>

        <!-- BODY -->
        <tr>
          <td style="padding:40px 40px 32px;">
            <h1 style="margin:0 0 8px;font-size:24px;font-weight:800;color:#042C53;">Verifica tu cuenta</h1>
            <p style="margin:0 0 24px;font-size:15px;color:#4A6A85;line-height:1.6;">
              Hola <strong>Jesús</strong>, gracias por registrarte en Opertrack.<br/>
              Haz clic en el botón para activar tu cuenta y comenzar tu prueba gratuita de <strong>14 días</strong>.
            </p>

            <!-- CTA BUTTON -->
            <table cellpadding="0" cellspacing="0" style="margin:0 0 28px;">
              <tr>
                <td style="background:linear-gradient(135deg,#185FA5,#042C53);border-radius:10px;padding:0;">
                  <a href="https://opertrack.com/verify?token=abc123xyz" 
                     style="display:inline-block;padding:14px 36px;font-size:16px;font-weight:700;color:#ffffff;text-decoration:none;letter-spacing:0.3px;">
                    ✅ Verificar mi cuenta →
                  </a>
                </td>
              </tr>
            </table>

            <!-- INFO BOX -->
            <table width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td style="background:#E6F1FB;border-radius:10px;padding:16px 20px;border-left:4px solid #185FA5;">
                  <p style="margin:0;font-size:13px;color:#185FA5;line-height:1.6;">
                    ⏰ Este enlace expira en <strong>24 horas</strong>.<br/>
                    🔒 Si no creaste esta cuenta, ignora este email.
                  </p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- FEATURES STRIP -->
        <tr>
          <td style="padding:0 40px 32px;">
            <table width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td width="33%" style="text-align:center;padding:16px 8px;background:#F8FAFC;border-radius:10px;">
                  <div style="font-size:24px;margin-bottom:6px;">💬</div>
                  <div style="font-size:12px;font-weight:700;color:#042C53;">Bot WhatsApp</div>
                </td>
                <td width="4%"></td>
                <td width="33%" style="text-align:center;padding:16px 8px;background:#F8FAFC;border-radius:10px;">
                  <div style="font-size:24px;margin-bottom:6px;">📍</div>
                  <div style="font-size:12px;font-weight:700;color:#042C53;">GPS en vivo</div>
                </td>
                <td width="4%"></td>
                <td width="33%" style="text-align:center;padding:16px 8px;background:#F8FAFC;border-radius:10px;">
                  <div style="font-size:24px;margin-bottom:6px;">⏱️</div>
                  <div style="font-size:12px;font-weight:700;color:#042C53;">Nómina auto</div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td style="background:#F8FAFC;border-top:1px solid #E2E8F0;padding:20px 40px;text-align:center;">
            <p style="margin:0;font-size:12px;color:#94A3B8;">
              © 2025 Opertrack · Hecho en República Dominicana 🇩🇴<br/>
              <a href="https://opertrack.com" style="color:#185FA5;text-decoration:none;">opertrack.com</a> · 
              <a href="https://opertrack.com/privacy" style="color:#185FA5;text-decoration:none;">Privacidad</a> · 
              <a href="https://opertrack.com/unsubscribe" style="color:#185FA5;text-decoration:none;">Cancelar suscripción</a>
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
"""

# ══════════════════════════════════════════════
#  TEMPLATE 2 — BIENVENIDA
# ══════════════════════════════════════════════
template_bienvenida = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/></head>
<body style="margin:0;padding:0;background:#F0F4F8;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#F0F4F8;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">

        <!-- HEADER -->
        <tr>
          <td style="background:linear-gradient(135deg,#042C53 0%,#185FA5 100%);padding:36px 40px;text-align:center;">
            <table cellpadding="0" cellspacing="0" style="margin:0 auto;">
              <tr>
                <td style="padding-right:12px;vertical-align:middle;">
                  <svg width="48" height="48" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="100" cy="100" r="88" fill="none" stroke="#378ADD" stroke-width="12"/>
                    <line x1="64" y1="132" x2="136" y2="132" stroke="#B5D4F4" stroke-width="4" stroke-linecap="round"/>
                    <rect x="64"  y="114" width="14" height="18" rx="3" fill="#B5D4F4"/>
                    <rect x="82"  y="100" width="14" height="32" rx="3" fill="#B5D4F4"/>
                    <rect x="100" y="82"  width="14" height="50" rx="3" fill="#E6F1FB"/>
                    <rect x="118" y="68"  width="14" height="64" rx="3" fill="#E6F1FB"/>
                    <line x1="70"  y1="128" x2="132" y2="64" stroke="white" stroke-width="5" stroke-linecap="round"/>
                    <polyline points="118,58 132,64 126,78" fill="none" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </td>
                <td style="vertical-align:middle;">
                  <span style="font-size:28px;font-weight:800;color:#ffffff;">Oper</span>
                  <span style="font-size:28px;font-weight:300;color:#85B7EB;">track</span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- BODY -->
        <tr>
          <td style="padding:40px 40px 24px;">
            <h1 style="margin:0 0 8px;font-size:26px;font-weight:800;color:#042C53;">
              ¡Bienvenido a Opertrack! 🎉
            </h1>
            <p style="margin:0 0 28px;font-size:15px;color:#4A6A85;line-height:1.7;">
              Hola <strong>Jesús</strong>, tu cuenta está activa y lista.<br/>
              Tienes <strong>14 días gratis</strong> para explorar todo el potencial de Opertrack.
            </p>

            <!-- PASOS -->
            <p style="margin:0 0 16px;font-size:14px;font-weight:700;color:#042C53;letter-spacing:0.5px;">EMPIEZA EN 3 PASOS:</p>

            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:28px;">
              <tr>
                <td style="padding:14px 16px;background:#F8FAFC;border-radius:10px;border-left:4px solid #185FA5;margin-bottom:10px;">
                  <table cellpadding="0" cellspacing="0">
                    <tr>
                      <td style="width:32px;height:32px;background:#185FA5;border-radius:50%;text-align:center;vertical-align:middle;color:white;font-weight:800;font-size:14px;">1</td>
                      <td style="padding-left:12px;font-size:14px;color:#042C53;font-weight:600;">Conecta tu número de WhatsApp Business</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr><td style="height:8px;"></td></tr>
              <tr>
                <td style="padding:14px 16px;background:#F8FAFC;border-radius:10px;border-left:4px solid #378ADD;">
                  <table cellpadding="0" cellspacing="0">
                    <tr>
                      <td style="width:32px;height:32px;background:#378ADD;border-radius:50%;text-align:center;vertical-align:middle;color:white;font-weight:800;font-size:14px;">2</td>
                      <td style="padding-left:12px;font-size:14px;color:#042C53;font-weight:600;">Agrega tu primer técnico con su número</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr><td style="height:8px;"></td></tr>
              <tr>
                <td style="padding:14px 16px;background:#F8FAFC;border-radius:10px;border-left:4px solid #10B981;">
                  <table cellpadding="0" cellspacing="0">
                    <tr>
                      <td style="width:32px;height:32px;background:#10B981;border-radius:50%;text-align:center;vertical-align:middle;color:white;font-weight:800;font-size:14px;">3</td>
                      <td style="padding-left:12px;font-size:14px;color:#042C53;font-weight:600;">El técnico escribe "hola" — el bot lo reconoce</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>

            <!-- CTA -->
            <table cellpadding="0" cellspacing="0" style="margin:0 0 8px;">
              <tr>
                <td style="background:linear-gradient(135deg,#185FA5,#042C53);border-radius:10px;">
                  <a href="https://opertrack.com/dashboard" 
                     style="display:inline-block;padding:14px 36px;font-size:16px;font-weight:700;color:#ffffff;text-decoration:none;">
                    Ir a mi panel →
                  </a>
                </td>
              </tr>
            </table>
            <p style="margin:8px 0 0;font-size:12px;color:#94A3B8;">¿Necesitas ayuda? Escríbenos por <a href="https://wa.me/18091234567" style="color:#185FA5;">WhatsApp</a></p>
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td style="background:#F8FAFC;border-top:1px solid #E2E8F0;padding:20px 40px;text-align:center;">
            <p style="margin:0;font-size:12px;color:#94A3B8;">
              © 2025 Opertrack · Hecho en República Dominicana 🇩🇴<br/>
              <a href="https://opertrack.com" style="color:#185FA5;text-decoration:none;">opertrack.com</a>
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
"""

# ══════════════════════════════════════════════
#  TEMPLATE 3 — RECIBO DE PAGO
# ══════════════════════════════════════════════
template_recibo = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/></head>
<body style="margin:0;padding:0;background:#F0F4F8;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#F0F4F8;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">

        <!-- HEADER -->
        <tr>
          <td style="background:linear-gradient(135deg,#042C53 0%,#185FA5 100%);padding:36px 40px;text-align:center;">
            <table cellpadding="0" cellspacing="0" style="margin:0 auto;">
              <tr>
                <td style="padding-right:12px;vertical-align:middle;">
                  <svg width="48" height="48" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="100" cy="100" r="88" fill="none" stroke="#378ADD" stroke-width="12"/>
                    <line x1="64" y1="132" x2="136" y2="132" stroke="#B5D4F4" stroke-width="4" stroke-linecap="round"/>
                    <rect x="64"  y="114" width="14" height="18" rx="3" fill="#B5D4F4"/>
                    <rect x="82"  y="100" width="14" height="32" rx="3" fill="#B5D4F4"/>
                    <rect x="100" y="82"  width="14" height="50" rx="3" fill="#E6F1FB"/>
                    <rect x="118" y="68"  width="14" height="64" rx="3" fill="#E6F1FB"/>
                    <line x1="70"  y1="128" x2="132" y2="64" stroke="white" stroke-width="5" stroke-linecap="round"/>
                    <polyline points="118,58 132,64 126,78" fill="none" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </td>
                <td style="vertical-align:middle;">
                  <span style="font-size:28px;font-weight:800;color:#ffffff;">Oper</span>
                  <span style="font-size:28px;font-weight:300;color:#85B7EB;">track</span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- RECIBO HEADER -->
        <tr>
          <td style="padding:32px 40px 0;">
            <table width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td>
                  <h1 style="margin:0 0 4px;font-size:22px;font-weight:800;color:#042C53;">Recibo de pago</h1>
                  <p style="margin:0;font-size:13px;color:#94A3B8;">Factura #OPT-2025-0042 · 23 Jun 2025</p>
                </td>
                <td style="text-align:right;">
                  <span style="background:#ECFDF5;color:#059669;font-size:12px;font-weight:700;padding:6px 14px;border-radius:20px;border:1px solid #A7F3D0;">
                    ✓ PAGADO
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- DETALLE -->
        <tr>
          <td style="padding:24px 40px;">
            <table width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #E2E8F0;border-radius:10px;overflow:hidden;">
              <!-- Header tabla -->
              <tr style="background:#F8FAFC;">
                <td style="padding:10px 16px;font-size:11px;font-weight:700;color:#94A3B8;letter-spacing:1px;">DESCRIPCIÓN</td>
                <td style="padding:10px 16px;font-size:11px;font-weight:700;color:#94A3B8;letter-spacing:1px;text-align:right;">MONTO</td>
              </tr>
              <!-- Item -->
              <tr style="border-top:1px solid #E2E8F0;">
                <td style="padding:14px 16px;">
                  <div style="font-size:14px;font-weight:600;color:#042C53;">Plan Growth — Junio 2025</div>
                  <div style="font-size:12px;color:#94A3B8;margin-top:2px;">Hasta 20 técnicos · Período: 23 Jun – 23 Jul 2025</div>
                </td>
                <td style="padding:14px 16px;text-align:right;font-size:14px;font-weight:600;color:#042C53;">$129.00</td>
              </tr>
              <!-- Total -->
              <tr style="background:#E6F1FB;border-top:2px solid #B5D4F4;">
                <td style="padding:14px 16px;font-size:15px;font-weight:800;color:#042C53;">Total pagado</td>
                <td style="padding:14px 16px;text-align:right;font-size:18px;font-weight:800;color:#185FA5;">$129.00 USD</td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- METODO DE PAGO -->
        <tr>
          <td style="padding:0 40px 32px;">
            <table width="100%" cellpadding="0" cellspacing="0" style="background:#F8FAFC;border-radius:10px;padding:14px 16px;">
              <tr>
                <td style="font-size:13px;color:#4A6A85;">
                  💳 Visa terminada en <strong>4242</strong> · 
                  Próximo cobro: <strong>23 Jul 2025</strong>
                </td>
                <td style="text-align:right;">
                  <a href="https://opertrack.com/billing" style="font-size:13px;color:#185FA5;text-decoration:none;font-weight:600;">Ver facturación →</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td style="background:#F8FAFC;border-top:1px solid #E2E8F0;padding:20px 40px;text-align:center;">
            <p style="margin:0;font-size:12px;color:#94A3B8;">
              © 2025 Opertrack · Hecho en República Dominicana 🇩🇴<br/>
              <a href="https://opertrack.com" style="color:#185FA5;text-decoration:none;">opertrack.com</a> · 
              <a href="https://opertrack.com/billing" style="color:#185FA5;text-decoration:none;">Gestionar suscripción</a>
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
"""

# ══════════════════════════════════════════════
#  ENVIAR LOS 3 EMAILS
# ══════════════════════════════════════════════
emails = [
    {
        "subject": "✅ Verifica tu cuenta de Opertrack",
        "html": template_verificacion,
        "label": "Verificación de cuenta"
    },
    {
        "subject": "🎉 Bienvenido a Opertrack — Tu cuenta está activa",
        "html": template_bienvenida,
        "label": "Bienvenida"
    },
    {
        "subject": "🧾 Recibo de pago — Plan Growth · Junio 2025",
        "html": template_recibo,
        "label": "Recibo de pago"
    }
]

print("🚀 Enviando emails de demo de Opertrack...\n")

for email in emails:
    payload = json.dumps({
        "from": f"Opertrack <{from_email}>",
        "to": [to_email],
        "subject": email["subject"],
        "html": email["html"]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            print(f"✅ [{email['label']}] enviado — ID: {result.get('id')}")
    except urllib.error.HTTPError as e:
        error = json.loads(e.read())
        print(f"❌ [{email['label']}] Error: {error}")

print("\n📬 Revisa tu bandeja de entrada en jesusgrullon20@gmail.com")
