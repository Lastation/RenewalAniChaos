import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {                        
            f.LineShape(cp, 1, "Target", 90 * f.loop[cp] + 45, 5, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Templar", 90 * f.loop[cp] + 45, 5, 50, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 3)
         {       
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 45 * 3 * f.loop[cp], 5, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Zealot", 45 * 3 * f.loop[cp], 5, 50, 0);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

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