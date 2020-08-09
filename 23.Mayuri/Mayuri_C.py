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
            f.NxNSquareShape(cp, 1, "40 + 1n Mojo", 3, 50);
            f.SquareShape(cp, 1, "40 + 1n Marine", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Marine", 0, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            
            f.SkillWait(cp, 80);
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 50 * f.loop[cp], 100);
            f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 50 * f.loop[cp], -100);
            f.DotShape(cp, 1, "40 + 1n Zealot", -100, 100 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", 100, -100 + 50 * f.loop[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 5, 100);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 4, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}