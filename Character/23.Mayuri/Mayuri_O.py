import Function as f;

const s = StringBuffer();

function main(cp)
{
   MoveLocation("23.Mayuri_Bozo", f.heroID[cp], cp, "Anywhere");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         SetSwitch("Recall - Mayuri", Set);

         if (cp < 3) SetSwitch("Unique - Mayuri1", Set);
         else SetSwitch("Unique - Mayuri2", Set);

         SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime");
         SetDeaths(cp, SetTo, 180, " `UniqueSkill");

         f.SkillWait(cp, 80);

         f.count[cp] += 1;
      }
      else if (f.count[cp] == 1)
      {
         SetSwitch("Recall - Mayuri", Clear);
         f.SkillEnd(cp);
      }
   }
}