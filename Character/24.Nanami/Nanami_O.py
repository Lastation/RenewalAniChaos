import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            if (cp < 3) SetSwitch("Unique - Nanami1", Set);
            else SetSwitch("Unique - Nanami2", Set);

            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            SetDeaths(cp, SetTo, 2160, " `UniqueCoolTime");
            SetDeaths(cp, SetTo, 720, " `UniqueSkill");

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillEnd(cp);
      }
   }
}