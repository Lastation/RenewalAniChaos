import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {                        
            f.LineShape(cp, 1, "Kakaru (Twilight)", 45 * 3 * f.loop[cp], 7, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Templar", 45 * 3 * f.loop[cp], 7, 50, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            f.SkillWait(cp, 50);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 0);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 2)
         {    
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 50);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 3, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 0);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }

      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}