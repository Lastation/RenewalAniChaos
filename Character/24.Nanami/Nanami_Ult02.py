import Function as f;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 12)
         {         
            f.SquareShape(cp, 1, "60 + 1n Archon", 200, 0);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 50);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 50, 150);
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 120);
            f.EdgeShape(cp, 1, "Target", 0, 4, 80);
            f.DotShape(cp, 24, "50 + 1n Tank", 0, 0);

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 120);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 3, 80);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 7, 160);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (cp < 3)
         {
            SetDeaths(P1, Add, 250, " `UltimateCoolTime");
            SetDeaths(P2, Add, 250, " `UltimateCoolTime");
            SetDeaths(P3, Add, 250, " `UltimateCoolTime");
            SetDeaths(cp, Subtract, 250, " `UltimateCoolTime");
         }
         else
         {
            SetDeaths(P4, Add, 250, " `UltimateCoolTime");
            SetDeaths(P5, Add, 250, " `UltimateCoolTime");
            SetDeaths(P6, Add, 250, " `UltimateCoolTime");
            SetDeaths(cp, Subtract, 250, " `UltimateCoolTime");   
         }

         f.SkillEnd(cp);
      }
   }
}