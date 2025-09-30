# Linux Deploy 2025 - Ubuntu Auto-Update System
## Upgrade Plan for Automatic Ubuntu Version Management

**Version:** 1.0  
**Date:** 2025-09-30  
**Objective:** Enable automatic installation of the latest Ubuntu LTS and interim versions instead of using hardcoded, outdated versions.

---

## 1. CURRENT UBUNTU LIMITATIONS

### 1.1 Hardcoded Ubuntu Versions

**Currently in arrays.xml:**
- 12.04 Precise Pangolin (EOL: April 2017)
- 14.04 Trusty Tahr (EOL: April 2019)
- 16.04 Xenial Xerus (EOL: April 2021)
- 18.04 Bionic Beaver (EOL: April 2023)

**Missing Modern Versions:**
- ❌ 20.04 Focal Fossa (LTS, supported until 2025)
- ❌ 22.04 Jammy Jellyfish (LTS, supported until 2027)
- ❌ 23.10 Mantic Minotaur (interim)
- ❌ 24.04 Noble Numbat (LTS, supported until 2029)
- ❌ 24.10 Oracular Oriole (interim)

**Critical Issues:**
1. All current versions are past EOL (End of Life)
2. Security vulnerabilities and no updates
3. Users cannot install modern Ubuntu without app update
4. Missing ARM64 optimizations in newer releases
5. No access to modern package versions

---

## 2. SIMPLE UBUNTU AUTO-UPDATE SOLUTION

### 2.1 How It Works

**Step 1:** Create a simple JSON file hosted on GitHub with current Ubuntu versions
**Step 2:** Android app downloads this file on startup (or weekly)
**Step 3:** User sees latest Ubuntu versions in the distribution selector
**Step 4:** Install proceeds with selected version

### 2.2 Components

#### **GitHub Metadata File (ubuntu.json)**
Simple JSON file with Ubuntu LTS and interim releases, updated manually or via script.

#### **Android Metadata Fetcher**
Small Java class that downloads and caches the JSON file.

#### **Updated UI**
Distribution selector shows current Ubuntu versions dynamically.

---

## 3. IMPLEMENTATION PLAN

### Phase 1: Create Ubuntu Metadata File (1 day)

**Create simple ubuntu.json file:**

Location: `https://raw.githubusercontent.com/[username]/linuxdeploy-ubuntu/main/ubuntu.json`

```json
{
  "name": "ubuntu",
  "last_updated": "2025-09-30",
  "releases": [
    {
      "suite": "noble",
      "version": "24.04",
      "name": "Noble Numbat",
      "lts": true,
      "recommended": true,
      "eol_date": "2029-04",
      "architectures": ["armhf", "arm64", "amd64", "i386"]
    },
    {
      "suite": "jammy",
      "version": "22.04",
      "name": "Jammy Jellyfish",
      "lts": true,
      "recommended": true,
      "eol_date": "2027-04",
      "architectures": ["armhf", "arm64", "amd64", "i386"]
    },
    {
      "suite": "focal",
      "version": "20.04",
      "name": "Focal Fossa",
      "lts": true,
      "recommended": false,
      "eol_date": "2025-04",
      "architectures": ["armhf", "arm64", "amd64", "i386"]
    }
  ],
  "mirrors": [
    "http://ports.ubuntu.com/ubuntu-ports",
    "http://archive.ubuntu.com/ubuntu"
  ]
}
```

### Phase 2: Create Simple Metadata Fetcher (1 week)

**New Java Class:** `UbuntuMetadataManager.java`

```java
public class UbuntuMetadataManager {
    private static final String UBUNTU_JSON_URL = 
        "https://raw.githubusercontent.com/[your-org]/linuxdeploy-ubuntu/main/ubuntu.json";
    
    private Context context;
    private SharedPreferences cache;
    
    // Fetch Ubuntu versions from GitHub
    public void fetchUbuntuVersions(Callback callback) {
        new AsyncTask<Void, Void, String>() {
            @Override
            protected String doInBackground(Void... voids) {
                try {
                    URL url = new URL(UBUNTU_JSON_URL);
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setConnectTimeout(5000);
                    
                    BufferedReader reader = new BufferedReader(
                        new InputStreamReader(conn.getInputStream()));
                    StringBuilder json = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        json.append(line);
                    }
                    reader.close();
                    return json.toString();
                } catch (Exception e) {
                    return null;
                }
            }
            
            @Override
            protected void onPostExecute(String json) {
                if (json != null) {
                    // Cache it
                    cache.edit().putString("ubuntu_releases", json)
                        .putLong("last_update", System.currentTimeMillis())
                        .apply();
                    callback.onSuccess(json);
                } else {
                    // Use cached or fallback to embedded
                    String cached = cache.getString("ubuntu_releases", null);
                    callback.onSuccess(cached != null ? cached : getEmbeddedUbuntu());
                }
            }
        }.execute();
    }
    
    // Parse JSON to get Ubuntu versions
    public List<UbuntuRelease> getUbuntuReleases() {
        String json = cache.getString("ubuntu_releases", getEmbeddedUbuntu());
        // Parse JSON and return list
    }
    
    // Fallback embedded Ubuntu versions
    private String getEmbeddedUbuntu() {
        return "{\"releases\":[{\"suite\":\"jammy\",\"version\":\"22.04\"}]}";
    }
}
```

### Phase 3: Update Arrays.xml (30 minutes)

**Modify:** `app/src/main/res/values/arrays.xml`

Add modern Ubuntu versions:
```xml
<string-array name="ubuntu_suite_values" translatable="false">
    <item>noble</item>      <!-- 24.04 LTS -->
    <item>jammy</item>      <!-- 22.04 LTS -->
    <item>focal</item>      <!-- 20.04 LTS -->
    <item>bionic</item>     <!-- 18.04 LTS (Keep for compatibility) -->
</string-array>
```

### Phase 4: Update PropertiesFragment (2 hours)

**Modify:** `PropertiesFragment.java`

```java
// On startup, fetch latest Ubuntu versions
UbuntuMetadataManager manager = new UbuntuMetadataManager(getContext());
manager.fetchUbuntuVersions(json -> {
    updateUbuntuSuiteList(); // Refresh UI with new versions
});
```

### Phase 5: Testing (1 day)

**Test:**
1. Install Ubuntu 24.04 on ARM64
2. Install Ubuntu 22.04 on ARM32
3. Test offline mode (cached versions)
4. Test fallback to embedded if network fails

---

## 4. QUICK START IMPLEMENTATION

### Step 1: Update arrays.xml Right Now (5 minutes)

Simplest approach - just add the new Ubuntu versions to the existing arrays.xml:

```xml
<!-- In app/src/main/res/values/arrays.xml -->
<string-array name="ubuntu_suite_values" translatable="false">
    <item>noble</item>      <!-- NEW: 24.04 LTS -->
    <item>jammy</item>      <!-- NEW: 22.04 LTS -->
    <item>focal</item>      <!-- NEW: 20.04 LTS -->
    <item>bionic</item>     <!-- KEEP: 18.04 LTS -->
    <item>xenial</item>     <!-- KEEP: 16.04 (for compatibility) -->
</string-array>
```

**Result:** Users can immediately install Ubuntu 24.04 and 22.04!

### Step 2: Add Auto-Update Later (Optional)

Once basic support is working, add the metadata fetcher for future updates without app releases.

This is **optional** and can be done later if you want automatic updates.

---

## 5. UBUNTU VERSION UPDATE PROCESS

### When Ubuntu Releases New Version

**Manual Update (Current):**
1. Edit `arrays.xml`
2. Add new suite name (e.g., "plucky" for 25.04)
3. Rebuild app
4. Release update

**Automated Update (Future - Optional):**
1. Update ubuntu.json on GitHub
2. Users' apps auto-fetch new version
3. No app rebuild needed

### Ubuntu Release Schedule
- **April:** New LTS (even years) or interim release
- **October:** Interim release

---

## 6. BENEFITS OF UBUNTU UPDATE

### For Users
✅ **Modern Ubuntu versions**: 24.04, 22.04, 20.04  
✅ **Better security**: Up-to-date packages and patches  
✅ **ARM64 optimizations**: Native support in newer releases  
✅ **Latest software**: Access to current package versions  
✅ **LTS support**: Long-term support until 2029 (24.04)  

### For Developers
✅ **5-minute fix**: Just update arrays.xml  
✅ **No complex infrastructure**: Simple solution first  
✅ **Optional automation**: Can add metadata system later  
✅ **Backward compatible**: Old versions still work  

---

## 7. SIMPLE TIMELINE

### Immediate Solution (Today)
⌛ **5 minutes:** Update arrays.xml with new Ubuntu versions  
⌛ **10 minutes:** Build and test  
⌛ **15 minutes:** Release update  

**Total:** 30 minutes to support Ubuntu 24.04!

### Future Enhancement (Optional)
⌛ **2-3 days:** Implement UbuntuMetadataManager  
⌛ **1 day:** Create ubuntu.json on GitHub  
⌛ **1 day:** Testing  

**Total:** ~1 week for auto-update system

---

## 8. TESTING CHECKLIST

### Before Release
- [ ] Install Ubuntu 24.04 Noble on ARM64 device
- [ ] Install Ubuntu 22.04 Jammy on ARM64 device  
- [ ] Install Ubuntu 20.04 Focal on ARM32 device
- [ ] Verify debootstrap works with ports.ubuntu.com mirror
- [ ] Check GUI installation (LXDE/XFCE)
- [ ] Verify SSH access
- [ ] Test with different disk sizes

### Known Issues
- Older Ubuntu mirrors may be slow
- ARM32 support ending in newer releases
- Some packages may differ between versions

---

## 9. IMMEDIATE ACTION ITEMS

### Option A: Quick Fix (Recommended)
1. Open `app/src/main/res/values/arrays.xml`
2. Add noble, jammy, focal to ubuntu_suite_values
3. Build APK and test
4. Release

### Option B: Full Solution
1. Do Option A first (get users unblocked)
2. Then implement UbuntuMetadataManager
3. Create GitHub repo with ubuntu.json
4. Add background update service

---

## 10. RECOMMENDED APPROACH

**Start Simple:**
- Update arrays.xml today (30 minutes)
- Release to users immediately
- They can install modern Ubuntu versions

**Enhance Later:**
- Add metadata system when you have time
- Enables updates without app releases
- Nice-to-have, not critical

**Result:** Users get Ubuntu 24.04 support today, automation comes later!

